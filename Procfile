web: gunicorn config.wsgi:application
worker: celery worker --app=cbf.taskapp --loglevel=info
