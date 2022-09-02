import os

import environ


env = environ.Env()
env.read_env('.env')

workers = env.int('GUNICORN_WEB_WORKERS', 1)
max_requests = env.int('GUNICORN_MAX_REQUESTS', 1000)
preload_app = True
accesslog = None
if env.bool('GUNICORN_ACCESS_LOG_ENABLE', default=False):
    accesslog = '-'

bind = 'unix:/tmp/nginx.socket'


def when_ready(server):
    # This file tells nginx that gunicorn is ready
    os.mknod('/tmp/app-initialized')
