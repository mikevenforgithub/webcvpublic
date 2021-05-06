heroku ps:scale web=1
web: gunicorn WEBCV.wsgi --log-file -
heroku config:set DISABLE_COLLECTSTATIC=1