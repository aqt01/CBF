release: ./release-tasks.sh 
web: gunicorn --pythonpath "$PWD/CBF" --capture-output CBF.wsgi:application --log-file -
worker: celery worker -B --scheduler django_celery_beat.schedulers:DatabaseScheduler --loglevel=DEBUG --workdir "./CBF" -A  CBF
