sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE Stepik_web_project;"
mysql -uroot -e "GRANT ALL PRIVILEGES ON Stepik_web_project.* TO 'box'@'localhost' WITH GRANT OPTION;"
python3 ask/manage.py makemigrations qa
python3 ask/manage.py migrate qa
sudo gunicorn -c hello.py hello:wsgi_app
sudo gunicorn -c etc/ask_conf.py ask.wsgi:application
