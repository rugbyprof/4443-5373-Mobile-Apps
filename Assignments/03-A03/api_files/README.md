## Api Starter

### Upload Files

Upload your files to your server: 

```bash
rsync -avz -e ssh ./api_files root@12.34.56.78:/root/api
# replace 12.34.56.78 with your ip address or domain name
```

#### Command Break Down

- `rsync`: The command to start the rsync utility.
- `-a`: This stands for "archive mode," which essentially preserves the file system permissions, timestamps, symbolic links, and other attributes.
- `-v`: This stands for "verbose," providing detailed output of the rsync command's progress.
- `-z`: This enables compression (`gzip` compression) of the data during the transfer, which can speed up the transfer of large files or folders.
- `-e ssh`: Specifies the use of SSH for the data transfer, enhancing security. This is particularly important since you're logging in as `root`.
- `./api_files`: The source directory you're uploading. The `./` prefix indicates that the folder is located in the current directory from where you're running the command. If it's in a different location, you'll need to specify the full or relative path.
- `root@12.34.56.78:/root/`: The destination where you're uploading the `api_files` folder. This syntax specifies the `root` user at the IP address `12.34.56.78`, and the folder will be uploaded into the `/root` directory on the server.
- Notice the word `api` != `api_files`. This just renames the folder at the destination. If we left off `api` it would keep the same folder.

A couple of things to remember:
- Ensure you have `rsync` installed on both your local machine and the server.
- Since you're using `root` for the transfer, make sure you have the necessary permissions and SSH access configured for the `root` user on the server. This often involves having the root user's public SSH key in the `/root/.ssh/authorized_keys` file on the server.
- Depending on your server's configuration, you might need to adjust firewall settings or `sshd_config` to allow root login over SSH, which is typically discouraged due to security considerations.

Using `rsync` in this way is super efficient and secure, especially with the `-z` option for compression and `-e ssh` for encrypted transfer. Just be careful with root access, as it comes with great power and responsibility!

### Dependencies

Install the requirements. Remember I have been creating a virtual environment in each of my project folders. So, that is the method I will be showing. 


### Setup

To set up a Python virtual environment (venv) on an Ubuntu server, you'll want to make sure you have Python and the `python3-venv` package installed. The `venv` module is part of the standard library in Python 3, but on Ubuntu, you might need to install it separately. Here's a step-by-step guide to get you sorted:

#### Step 1: Install python3-venv

Once Python 3 is set up, you can install the `python3-venv` package, which includes the `venv` module, by running:

```bash
sudo apt install python3-venv
```

#### Step 2: Create a Virtual Environment

Now that you have all the necessary tools, choose a directory where you want to create your virtual environment. Then, run the following command to create a virtual environment. In this example, I'm naming the environment `myenv`, but you can name it whatever you prefer. I name mine `.venv`, but its just my preference. Some devs name the venv more inline with the project, like `apivenv`:

```bash
python3 -m venv myenv
```

This command will create a `myenv` directory if it doesn't exist and set up a new virtual environment inside it.

### Step 3: Activate the Virtual Environment

To start using this virtual environment, you need to activate it. To do so, run:

```bash
source myenv/bin/activate
```

Once activated, your terminal prompt will change to indicate that you're now working inside the `myenv` virtual environment. While activated, any Python or pip commands will use the versions in the virtual environment, not the global Python installation.

### Step 4: Install Requirements

Install the requirements for the Fast Api code:

```bash
pip install -r requirements.txt
```

This will install everything listed in the `requirements.txt` folder.

### Step 5: Run Api

- Change the IP address at the bottom of api.py to your ip address.
- Make sure 8080 is opened through the firewall.
- Run python api.py

Hopefully its running, go access it in a browser with: [http://your.ip.address:8080](http://your.ip.address:8080)


### Step 6: Deactivating the Virtual Environment

When you're done working in the virtual environment and want to return to your global Python environment, simply run:

```bash
deactivate
```

This command deactivates the virtual environment, and your terminal prompt will return to normal, indicating you're no longer in the virtual environment.




