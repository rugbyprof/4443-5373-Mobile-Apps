import pika

class RabbitMQClient:
    def __init__(self, url, username, password):
        credentials = pika.PlainCredentials(username, password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(url, credentials=credentials))
        self.channel = self.connection.channel()
    
    def close(self):
        self.connection.close()

# Admin class for managing RabbitMQ resources, stub only
class RabbitMQAdmin(RabbitMQClient):
    def create_user(self, username, password):
        # Implement user creation via RabbitMQ's HTTP API
        pass

    def create_exchange(self, exchange_name):
        # Create an exchange
        self.channel.exchange_declare(exchange=exchange_name, exchange_type='topic')
    
    def create_queue(self, queue_name):
        # Create a queue
        self.channel.queue_declare(queue=queue_name)

# Producer class for sending messages
class MessageSender(RabbitMQClient):
    def send_message(self, exchange, routing_key, message):
        self.channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message)

# Consumer class for receiving messages
class MessageReceiver(RabbitMQClient):
    def start_consuming(self, queue_name, callback):
        self.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()

# Example usage:
# admin = RabbitMQAdmin('url', 'username', 'password')
# admin.create_exchange('chatExchange')
# admin.create_queue('chatQueue')

# sender = MessageSender('url', 'username', 'password')
# sender.send_message('chatExchange', 'chatRoutingKey', 'Hello, world!')

# def callback(ch, method, properties, body):
#     print(f"Received {body}")
# receiver = MessageReceiver('url', 'username', 'password')
# receiver.start_consuming('chatQueue', callback)
