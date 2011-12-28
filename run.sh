#!/bin/bash
set -e
LOGFILE=/var/log/gunicorn/django_app.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3  #recommended formula here is 1 + 2 * NUM_CORES
 
#we don't want to run this as root..
USER=www-data
GROUP=www-data
 
cd /home/ubuntu/django_app
source bin/activate
cd app
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn_django -w $NUM_WORKERS \
  --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE \
  --user=$USER --group=$GROUP
