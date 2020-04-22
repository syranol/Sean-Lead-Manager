heroku config:set DISABLE_COLLECTSTATIC=1

release: python manage.py migrate
web: gunicorn leadmanager.wsgi.application.wsgi --log-file -
