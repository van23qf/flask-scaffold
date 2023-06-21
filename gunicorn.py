# gunicorn配置文件
from gevent import monkey

monkey.patch_all()

import os
from environs import Env

env = Env()
env.read_env()
port = env.str('PORT') if env.str('PORT') else 9000

# 工作模式，默认sync模式
# worker_class = 'gunicorn.workers.ggevent.GeventWorker'
worker_class = 'gevent'
# worker_class = 'sync'
# 并行进程数
workers = 1
# 每个进程的线程数
threads = 1
# 内网IP和端口
bind = '0.0.0.0:9300'
# 是否后台守护模式
daemon = 'false' if os.environ.get('PROJECT_RUNTIME_ENV') == 'docker' else 'true'
daemon = 'false'
# 最大并发量
worker_connections = port
# 日志
# accesslog = './logs/gunicorn_access.log'
# errorlog = './logs/gunicorn_error.log'
loglevel = 'warning'
# 超时时间
timeout = 30
