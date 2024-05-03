"""
Basically queues can be binded to an exchange based on routingKeys.

Assume that you have 3 different publishers.
Publisher1 sending message to exchange with routingKey "events"
Publisher2 sending message to exchange with routingKey "tasks"
Publisher3 sending message to exchange with routingKey "jobs"

You can have a consumer that consumes only messages with specific routhingKey.
For example in order to have a consumer for "events" messages you declare like this

 channel.queueBind(queueName, exchangeName, "events");
If you want to consume all the messages coming to the exchange you give the routing as '#'

So in short what i can say is,
1. Messages will be published to an exchange.
2. Queues will be bound to exchange based on routingKeys.
3. RabbitMQ will forward messages with matching routing keys to the corresponding queues.

Please
"""

import json
import os
import sys
import time
import pika
import random
from threading import Thread
from rich import print
import requests
import subprocess


# # Execute in command line
# def countConnections():
#     command = "curl -i -u admin:1922msuQAZ!! http://terrywgriffin:15672/api/queues/"
#     proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
#     script_response = proc.stdout.read().split("\n")
#     resp = json.loads(script_response[7])
#     return resp


def isJson(myjson):
    try:
        json.loads(myjson)
    except ValueError as e:
        return False
    return True


# Usage example:
# amqp_url = 'amqp://user:password@localhost'
# sender = DirectMessageSender(amqp_url)
# sender.send('routing_key', 'Hello RabbitMQ!')
# sender.close()


class DirectMessageSender:
    def __init__(self, user, password, url="chat.sendmessage.live", exchange="chat"):
        amqp_url = f"amqp://{user}:{password}@{url}"
        self.connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
        self.channel = self.connection.channel()
        self.exchange = exchange

        # Ensure the exchange exists. For direct messaging, you might use the default ('') exchange.
        self.channel.exchange_declare(
            exchange=self.exchange, exchange_type="direct", durable=True
        )

    def send(self, routing_key, message):
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=routing_key,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ),
        )

    def close(self):
        self.connection.close()


# Usage example:
# amqp_url = 'amqp://user:password@localhost'
# receiver = DirectMessageReceiver(amqp_url, 'user_queue')
# receiver.start()
# Do something else here or just wait; the receiver runs on its own thread.
# receiver.close()  # When you're ready to stop.


class DirectMessageReceiver:
    def __init__(self, user, password, queue_name, url="chat.sendmessage.live"):
        amqp_url = f"amqp://{user}:{password}@{url}"
        self.connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
        self.channel = self.connection.channel()

        # Ensure the queue exists. This is idempotent.
        self.channel.queue_declare(queue=queue_name, durable=True)

        self.queue_name = queue_name

    def on_message(self, ch, method, properties, body):
        print(f"Received message: {body.decode()}")
        # Here, implement what you want to do with the message

    def start_consuming(self):
        self.channel.basic_consume(
            queue=self.queue_name, on_message_callback=self.on_message, auto_ack=True
        )
        print(f"[*] Waiting for messages in {self.queue_name}. To exit press CTRL+C")
        self.channel.start_consuming()

    def start(self):
        thread = Thread(target=self.start_consuming)
        thread.start()

    def close(self):
        self.connection.close()


class MQConnect(object):
    """This base class simply connects to the rabbitmq server and is used by both the sender
    and listener classes.
    """

    def __init__(self, **kwargs):
        """Remember keyword arguments are params like: key=arg and order doesn't matter. Here is an
        example connection:

        comms = Comms(
            exchange="2dgame",
            port="5672",
            host="crappy2d.us",
            user="yourteamname",
            password= "yourpassword"
        )
        """
        self.exchange = kwargs.get("exchange", None)
        self.port = kwargs.get("port", 5432)
        self.host = kwargs.get("host", None)
        self.user = kwargs.get("user", None)
        self.password = kwargs.get("password", None)
        self.binding_keys = kwargs.get("binding_keys", [])
        self.messageQueue = {}

        self.setupConnection()

    def setupConnection(self, **kwargs):
        """This method basically authenticates with the message server using:

                exchange: the 'channel' we will send messages on
                host: the ip address or domain name of the server
                port: port number (nearly always 5672)
                user: your username
                password: your password

        After authentication it chooses which "exchange" to listen to. This
        is just like a "channel" in slack. The exchange "type" = "topic" is
        what allows us to use key_bindings to choose which messages to recieve
        based on keywords.
        """
        self.exchange = kwargs.get("exchange", self.exchange)
        self.port = kwargs.get("port", self.port)
        self.host = kwargs.get("host", self.host)
        self.user = kwargs.get("user", self.user)
        self.password = kwargs.get("password", self.password)

        # names is a list of expected keys to be passed in that I
        # use for error checking,
        names = ["exchange", "port", "host", "user", "password"]
        params = [self.exchange, self.port, self.host, self.user, self.password]

        # p[0] is the key and p[1] is the value
        for p in zip(names, params):
            if not p[1]:
                print(
                    f"Error: connection parameter `{p[0]}` missing in class Comms method `setupConnection`!"
                )
                sys.exit()

        # establish credentials and auth values
        credentials = pika.PlainCredentials(self.user, self.password)
        self.parameters = pika.ConnectionParameters(
            self.host, int(self.port), self.exchange, credentials, heartbeat=60
        )

        self.connect()

    def connect(self):
        try:
            self.connection = pika.BlockingConnection(self.parameters)
            self.channel = self.connection.channel()
            self.channel.exchange_declare(exchange=self.exchange, exchange_type="topic")
        except pika.exceptions.AMQPConnectionError:
            time.sleep(2)
            self.connect()


class MQListener(MQConnect):
    def __init__(self, **kwargs):
        """Extends base class MQConnect."""
        self.binding_keys = kwargs.get("binding_keys", [])

        super().__init__(**kwargs)

    def bindKeysToQueue(self, binding_keys=None):
        """https://www.rabbitmq.com/tutorials/tutorial-five-python.html

        A binding key is a way of "subscribing" to a specific messages. Without
        getting to the difference between "routing" and "topics". The example below
        shows how a routing key can include multiple items and be directed based on any
        of the words below:

           python.javascript.cpp

        This topic would receive any messages from queues containing the routing
        keys: `python` or `javascript` or `cpp`. You can register as many keys as you like.
        But you can also use wild cards:

            * (star) can substitute for exactly one word.
            # (hash) can substitute for zero or more words.

        So if you want to get all messages with your team involved:
            teamname.#
        Or if you want all messages that fire at you:
            teamname.fire.#
        Or if you want to send a message to everyone:
            broadcast.#

        Follow the link above to get a better idea, but at minimum you should
        add binding keys for anything with your teamname (or maybe id) in it.

        """
        self.queueState = self.channel.queue_declare("", exclusive=True)
        self.queue_name = self.queueState.method.queue

        if binding_keys == None and len(self.binding_keys) == 0:
            self.binding_keys = ["#"]
        elif binding_keys:
            self.binding_keys = binding_keys

        for binding_key in self.binding_keys:
            # print(binding_key)
            self.channel.queue_bind(
                exchange=self.exchange, queue=self.queue_name, routing_key=binding_key
            )

    def startConsuming(self, callback=None):
        if not callback:
            callback = self.callback
        self.channel.basic_consume(
            queue=self.queue_name, on_message_callback=callback, auto_ack=True
        )
        self.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        """
        Description:
            - This method gets run when a message is received. You can alter it to do whatever is necessary.

        """

        if isJson(body):
            tmp = json.loads(body)
        if "from" in tmp:
            if not tmp["from"] in self.messageQueue:
                self.messageQueue[tmp["from"]] = []
            self.messageQueue[tmp["from"]].append(f"{body}")

        print(self.messageQueue)

    def threadedListen(self, callback=None):
        self.bindKeysToQueue([f"#.{self.user}.#", "#.broadcast.#"])
        Thread(
            target=self.startConsuming,
            args=(callback,),
            daemon=True,
        ).start()


class MQSender(MQConnect):
    def __init__(self, **kwargs):
        """Extends Comms and adds a "send" method which sends data to a
        specified channel (exchange).
        """
        super().__init__(**kwargs)

    def send(self, target, sender, body, closeConnection=True):
        # print(f"Sending: target: {target}, body: {body}")

        body = json.loads(body)

        body["from"] = sender

        try:
            self.publish(target, body)
        except pika.exceptions.AMQPConnectionError:
            self.connect()
            self.publish(target, body)

        if closeConnection:
            self.connection.close()

    def publish(self, target, body):
        """Publish msg"""

        self.channel.basic_publish(
            self.exchange, routing_key=target, body=json.dumps(body)
        )

    def threadedSend(self, **kwargs):
        """Immediately calls send with a thread."""
        target = kwargs.get("target", "broadcast")
        sender = kwargs.get("sender", "unknown")
        body = kwargs.get("body", {})
        closeConnection = kwargs.get("closeConnection", False)
        debug = kwargs.get("debug", False)

        if debug:
            print(f"Calling send via Thread")

        Thread(
            target=self.send,
            args=(
                target,
                sender,
                body,
                closeConnection,
            ),
            daemon=True,
        ).start()

    def closeConnection(self):
        self.connection.close()


def usage():
    print("Error: You need to choose `send` or `listen` and optionally `teamName`!")
    print("Usage: python CommsClass <send,listen>")
    sys.exit()


def mykwargs(argv):
    """
    Processes argv list into plain args and kwargs.
    Just easier than using a library like argparse for small things.
    Example:
        python file.py arg1 arg2 arg3=val1 arg4=val2 -arg5 -arg6 --arg7
        Would create:
            args[arg1, arg2, -arg5, -arg6, --arg7]
            kargs{arg3 : val1, arg4 : val2}

        Params with dashes (flags) can now be processed seperately
    Shortfalls:
        spaces between k=v would result in bad params
    Returns:
        tuple  (args,kargs)
    """
    args = []
    kwargs = {}

    for arg in argv:
        if "=" in arg:
            key, val = arg.split("=")
            kwargs[key] = val
        else:
            args.append(arg)
    return args, kwargs


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()

    args, kwargs = mykwargs(sys.argv)

    user = kwargs.get("user", "player-1")
    passwd = user + "2023!!!!!"
    # passwd = kwargs.get('passwd','player-12023!!!')
    target = kwargs.get("target", "player-2")
    # cmd = kwargs.get('cmd','message')
    # body = kwargs.get('body','hello world')
    method = kwargs.get("method", "listen")
    exchange = kwargs.get("exchange", "game1")

    creds = {
        "exchange": exchange,
        "port": "5672",
        "host": "terrywgriffin.com",
        "user": user,
        "password": passwd,  # user.capitalize() * 3,
    }

    if method == "send":
        exampleMessages = [
            {"cmd": "message", "body": {"messageTxt": "hello world"}},
            {
                "cmd": "move",
                "body": {
                    "startLon": 34.1234,
                    "startLat": -98.452,
                    "endLon": 34.1234,
                    "endLat": -98.452,
                },
            },
            {"cmd": "move", "body": {"dx": -4, "dy": 4}},
            {"cmd": "fire", "body": {"angle": 23, "velocity": 320}},
            {"cmd": "move", "body": {"dx": -4, "dy": 4, "angle": 231}},
        ]

        users = ["player-1", "player-2", "player-3", "player-4", "player-5"]
        vhosts = ["vhost1", "vhost2", "vhost3", "vhost4", "vhost5"]

        senders = []

        for i in range(1, 10):
            id = (i % 2) + 1
            user = f"player-{id}"
            creds["user"] = user
            creds["password"] = user + "2023!!!!!"

            creds["exchange"] = f"game{id}"
            print(creds)
            senders.append(MQSender(**creds))

            # cmd = random.choice(body[cmd])
            # data = random.choice(body[cmd])
            senders[-1].send(
                target=user,
                sender=user,
                body=json.dumps(random.choice(exampleMessages)),
            )
            time.sleep(2)

    else:
        print("Comms Listener starting. To exit press CTRL+C ...")

        commsListener = MQListener(**creds)
        # m = MultiComms('player-4','game1')
        commsListener.bindKeysToQueue([f"#.{user}.#", "#.broadcast.#"])
        commsListener.startConsuming()
