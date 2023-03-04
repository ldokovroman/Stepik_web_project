sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -c hello.py hello:wsgi_app
sudo gunicorn -c etc/ask_conf.py ask.wsgi:application