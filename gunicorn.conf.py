"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count


bind = '0.0.0.0:6000'
worker_class = 'gevent'
workers = cpu_count()
max_requests = 1000
worker_connections = 10000
max_requests_jitter = 5