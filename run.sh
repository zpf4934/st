#!/bin/bash
ANACONDA_PATH="/root/miniconda3/envs/stock/bin"


nohup $ANACONDA_PATH/python monitor_run.py --function monitor_mark monitor_pepb > nohup.out 2>&1 &

$ANACONDA_PATH/gunicorn --chdir /mnt/mac/stock_django -w 5 -b 0.0.0.0:8000 stock_django.wsgi:application
