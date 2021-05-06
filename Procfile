heroku ps:scale web=1
heroku run rails console 
heroku config:set DISABLE_COLLECTSTATIC=1
web: gunicorn WEBCV.wsgi --log-file -
