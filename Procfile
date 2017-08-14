release: python manage.py migrate --settings CBF.conf.production
web: gunicorn --pythonpath "$PWD/CBF" --capture-output CBF.wsgi:application --log-file -
