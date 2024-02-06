## Keep Api Alive

To ensure your FastAPI application stays up and running and automatically restarts after a crash, you can use:

### Process managers for linux

-  **systemd** 
-  or
-  **Supervisor**

### Containerization  

-  **Docker** combined with an orchestrator like 
   -  **Kubernetes** 
   -  or 
   -  **Docker Compose**

Each of these methods offers different levels of control, complexity, and features. We won't be doing any containerization, but I wanted to list it since it's pretty much what's done in industry to allow for fast deployment of systems, microservices, and scaling of systems


### Using systemd

For Linux systems, `systemd` is a common and powerful init system and system manager that can be used to start, stop, and manage services, including ensuring that your FastAPI application restarts on failure.

- **Create a systemd service file** for your application, typically located at `/etc/systemd/system/your_app.service`.

    ```ini
    [Unit]
    Description=FastAPI app
    After=network.target

    [Service]
    User=your_user
    WorkingDirectory=/path/to/your/app
    ExecStart=/path/to/your/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
    Restart=on-failure

    [Install]
    WantedBy=multi-user.target
    ```

- **Enable and start** the service:

    ```bash
    sudo systemctl enable your_app.service
    sudo systemctl start your_app.service
    ```

- The `Restart=on-failure` directive tells systemd to restart your service if it crashes.

### Using Supervisor

Supervisor is a process control system for UNIX-like operating systems. It allows you to monitor and control a number of processes on UNIX-like operating systems.

- **Install Supervisor** (if it's not already installed):

    ```bash
    sudo apt-get install supervisor
    ```

- **Create a configuration file** for your FastAPI application in `/etc/supervisor/conf.d/your_app.conf`.

    ```ini
    [program:your_app]
    command=/path/to/your/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
    directory=/path/to/your/app
    user=your_user
    autostart=true
    autorestart=true
    stderr_logfile=/var/log/your_app/your_app.err.log
    stdout_logfile=/var/log/your_app/your_app.out.log
    ```

- **Update Supervisor** with the new program and **start it**:

    ```bash
    sudo supervisorctl reread
    sudo supervisorctl update
    sudo supervisorctl start your_app
    ```

### Using Docker

Containerizing your FastAPI application with Docker can provide isolation, ease of deployment, and scalability. Docker can automatically restart containers that exit due to an error.

- **Create a Dockerfile** in your FastAPI application directory:

    ```Dockerfile
    FROM python:3.9
    WORKDIR /app
    COPY . /app
    RUN pip install fastapi uvicorn
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
    ```

- **Build and run your Docker container** with the `--restart` policy:

    ```bash
    docker build -t your_app .
    docker run -d --name your_fastapi_app -p 8000:80 --restart unless-stopped your_app
    ```

### Using Docker Compose

If you prefer Docker and want to manage multiple containers (e.g., your FastAPI app and a database), Docker Compose is an excellent tool.

- **Create a `docker-compose.yml`** file in your application directory:

    ```yaml
    version: '3.8'
    services:
      fastapi_app:
        build: .
        command: uvicorn main:app --host 0.0.0.0 --port 80
        ports:
          - "8000:80"
        restart: unless-stopped
    ```

- **Start your services** with Docker Compose:

    ```bash
    docker-compose up -d
    ```

Each of these methods ensures that your FastAPI application remains available, automatically restarting it after a failure. The choice of method depends on your specific requirements, infrastructure, and familiarity with the tools. For simple deployments, `systemd` or Supervisor might be sufficient, while Docker provides more flexibility and is better suited for complex deployments or microservices architectures.