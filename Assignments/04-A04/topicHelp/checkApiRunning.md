Sure thing, Terry! Below are the commands you'd typically use on a Linux system with UFW (Uncomplicated Firewall) to enable the firewall, open up ports for SSH (port 22), HTTPS (port 443), and a range of ports from 8080 to 8085. I'll also show you how to check if these ports are open and how to see which services are listening on these ports.

### Enable UFW

First, enable UFW. This command starts the firewall and ensures it starts on boot:

```sh
sudo ufw enable
```

### Allow SSH (Port 22)

To allow SSH connections (important if you're configuring a remote server to ensure you don't lock yourself out):

```sh
sudo ufw allow ssh
```
Or:
```sh
sudo ufw allow 22
```

### Allow HTTPS (Port 443)

To allow HTTPS traffic:

```sh
sudo ufw allow https
```
Or:
```sh
sudo ufw allow 443
```

### Allow Ports 8080 to 8085

To allow a range of ports (8080 to 8085) for both TCP and UDP traffic (adjust according to your specific needs, but most web services use TCP):

```sh
sudo ufw allow 8080:8085/tcp
sudo ufw allow 8080:8085/udp
```

### Check Status

To check the status of UFW and see which rules are active (including ports):

## Firewall

```sh
sudo ufw status
```
Or for a more detailed view:
```sh
sudo ufw status verbose
```

## Check Listening Services by Port

To see which services are listening on which ports, you can use the `ss` or `netstat` commands. For simplicity and clearer output, `ss` is usually preferred:

```sh
sudo ss -tuln
```

- `-t` for TCP
- `-u` for UDP
- `-l` for listening sockets
- `-n` for showing numerical addresses instead of trying to determine symbolic host, port, or user names
- `-p` for finding the process name attached to a port

This command will show you a list of all listening ports and the corresponding addresses. To filter this list to find specific ports or services, you can use `grep`, for example:

```sh
sudo ss -tulnp | grep ':22'
```

This command would show you if anything is listening on port 22 (SSH), and you can adjust the port number in the `grep` command to check other ports.

Remember, managing firewall settings and opening ports can expose your system to security risks if not done cautiously. Ensure you only open the ports you need for your applications and always use secure, authenticated, and encrypted protocols to protect your data in transit.

## Check Listening Services by Process

To perform a sort of 'reverse' lookup with the `ss` command, where you start with a process name (like `python`, `apache2`, or `nginx`) and want to find all the ports being listened to by that process, you can still use `ss` in combination with `grep`. However, because `ss` by itself doesn't directly allow you to filter by process name, the trick is to use `grep` to filter the output of `ss` based on the process information.

Here's how you can do it:

### For Python:

```sh
sudo ss -tulnp | grep 'python'
```

### For Apache2:

```sh
sudo ss -tulnp | grep 'apache2'
```

### For Nginx:

```sh
sudo ss -tulnp | grep 'nginx'
```

These commands will show you all listening sockets (`-l`), both TCP and UDP (`-tu`), without resolving service names (`-n`), and include the process name (`-p`) that matches the search term provided to `grep`. The output will be filtered to only show lines that contain the process name you're interested in.

### Important Note:

- Running `ss` with `-p` requires `sudo` or root privileges to see processes owned by other users.
- The process name shown in the `ss` output is the command as it was invoked, so if your service has a different name in the process list than what you're grepping for, you might need to adjust your search term. For example, some Python applications might be run with a specific script or module name.

### Additional Tip:

If you're interested in a more dynamic approach, especially if you're scripting, you can use the `pidof` command to find the PID of a process by name and then use that PID with `ss`. Here's an example workflow for `nginx`:

```sh
PIDS=$(pidof nginx)
for PID in $PIDS; do
    sudo ss -tulnp | grep "pid=$PID"
done
```

This approach first captures the PIDs of all `nginx` processes and then iterates over them, filtering the `ss` output for each PID. This can be particularly useful for processes that might spawn multiple instances.

These techniques give you flexibility in monitoring and managing your system's network connections, especially for troubleshooting or ensuring that your services are correctly configured to listen on the expected ports.

```python
import psutil
import sys
def find_python_process_ports(name='python'):
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cmdline', 'connections']):
        if name in proc.info['name']:
            connections = proc.connections(kind='inet')
            if connections:  # Check if the process has any internet connections
                for conn in connections:
                    if conn.status == psutil.CONN_LISTEN:
                        # Print out the PID, listening port and address, and command line
                        print(f"PID: {proc.pid}, Name: {name}, Listening on: {conn.laddr}, Command: {' '.join(proc.info['cmdline'])}>
                    else:
                        print(f"NAME: {name} not found!")


find_python_process_ports("python")
find_python_process_ports("https")
find_python_process_ports("ssh")
find_python_process_ports("apache")
```



