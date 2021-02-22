
#!/bin/bash
python manage.py collectstatic --noinput &&
python manage.py migrate 
#&& gunicorn NijiTest.wsgi:application -c gunicorn.conf
