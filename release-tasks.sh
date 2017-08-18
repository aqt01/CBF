python CBF/manage.py migrate --settings CBF.conf.production
python manage.py loaddata CBF/fixtures.json --settings CBF.conf.production
python CBF/manage.py populate-sermons --settings CBF.conf.production
