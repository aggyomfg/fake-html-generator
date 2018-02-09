# fake-html-generator

How to run (alpine linux):
/usr/sbin/uwsgi --plugins-dir /usr/lib/uwsgi/ --need-plugin python3 --http-socket 127.0.0.1:8080 --wsgi-file ./main.py