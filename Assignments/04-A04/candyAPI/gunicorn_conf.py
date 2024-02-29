# gunicorn_conf.py
from multiprocessing import cpu_count

bind = "kidsinvans.fun:8084"

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/var/log/fastapi/access_log/access.log'
errorlog =  '/var/log/fastapi/error_log/error.log'
