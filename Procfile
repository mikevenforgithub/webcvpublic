heroku ps:scale web=1
web: gunicorn WEBCV.wsgi --log-file -
heroku run rails console 
heroku config:set DISABLE_COLLECTSTATIC=1