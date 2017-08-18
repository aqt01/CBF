python CBF/manage.py migrate --settings CBF.conf.production
python CBF/manage.py loaddata CBF/CBF/fixtures.json --settings CBF.conf.production
python CBF/manage.py populate-sermons --settings CBF.conf.production
