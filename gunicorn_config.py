command = '/home/www/projects/laser_remover_back/env/bin/gunicorn'
pythonpath = '/home/www/projects/laser_remover_back/back'
bind = 'localhost:8000'
workers = 3
user = 'www'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=back.settings'
