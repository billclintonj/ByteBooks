# This file should be passed as an argument when gunicorn wsgi server is used
# $ /usr/local/bin/gunicorn -c gunicorn_conf.py e_commerce.wsgi
bind = '0.0.0.0:8000'
worker_class = 'sync'
loglevel = 'debug'
accesslog = '/var/log/gunicorn/access_log_ebooks'
acceslogformat ="%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s"
errorlog =  '/var/log/gunicorn/error_log_ebooks'