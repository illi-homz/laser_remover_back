#!/bin/bash

source /home/www/projects/tatu_by_laser_remover/back/env/bin/activate
#source /home/www/projects/tatu_by_laser_remover/back/env/bin/postactivate
exec gunicorn  -c "/home/www/projects/tatu_by_laser_remover/back/gunicorn_config.py" back.wsgi
