
# Commands

psql -U postgres -d testdb      
\dt
exit
\q

python manage.py createsuperuser
python manage.py runserver

OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES gunicorn backend.wsgi:application --bind 0.0.0.0:8000
python manage.py collectstatic

DJANGO_SECRET_KEY=django-insecure-b-vu@p4qfnwf)0vqj1m-)88)r@c)$y1mn6#fov@^hom+%wjg!+
"ENGINE": "django.db.backends.postgresql",
"NAME": os.environ.get("DB_NAME", "testdb"),         # Falls back to local testdb
"USER": os.environ.get("DB_USER", "postgres"),
"PASSWORD": os.environ.get("DB_PASSWORD", "postgres"),
"HOST": os.environ.get("DB_HOST", "localhost"),
"PORT": os.environ.get("DB_PORT", "5432"),

https://github.com/Parth2k3/test-django

source venv/bin/activate
pip3 install django
pip3 install gunicorn
pip3 install django-cors-headers
pip3 install djangorestframework whitenoise
gunicorn --bind 0.0.0.0:8000 backend.wsgi:application

cd /etc/nginx/sites-available
sudo nano django_app
server {
    listen 80;
    server_name 3.75.86.179;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
sudo ln -s /etc/nginx/sites-available/django_app /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx
sudo nano /etc/systemd/system/django_app.service

[Unit]
Description=Gunicorn instance for django app
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/test-django
ExecStart=/home/ubuntu/test-django/venv/bin/gunicorn -w 3 --bind 0.0.0.0:8000 
test.wsgi:application
Restart=always

[Install]
WantedBy=multi-user.target

sudo systemctl daemon-reload
sudo systemctl enable django_app
sudo systemctl start django_app
sudo systemctl status django_app
sudo systemctl reload nginx
sudo systemctl restart nginx
cd ~

sudo systemctl stop django_app
sudo systemctl daemon-reload
sudo systemctl restart django_app
sudo journalctl -u django_app.service -f

# Clear the "failed" status
sudo systemctl reset-failed django_app

# Reload the configuration
sudo systemctl daemon-reload

# Start it back up
sudo systemctl start django_app

sudo systemctl status django_app

# Security

sudo apt update
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d api.dasha-tristan-wedding.com
sudo cat /etc/nginx/sites-enabled/default
sudo nano /etc/nginx/sites-available/django_app

server {
    listen 80;
    server_name dasha-tristan-wedding.com;
    return 301 https://$host$request_uri; # Redirects HTTP to HTTPS
}

server {
    listen 443 ssl; 
    server_name dasha-tristan-wedding.com;

    ssl_certificate /etc/letsencrypt/live/dasha-tristan-wedding.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/dasha-tristan-wedding.com/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /home/ubuntu/wedding_backend/staticfiles/;
    }
}

# Remove the default link if it exists
sudo rm /etc/nginx/sites-enabled/default

# Ensure your django_app is linked (if not already)
sudo ln -s /etc/nginx/sites-available/django_app /etc/nginx/sites-enabled/

# Test and Restart
sudo nginx -t
sudo systemctl restart nginx

1. The Standard "Best Practice" SetupTo make everything work smoothly without errors, you should assign them like this:URLWho uses it?Where does it point?www.dasha-tristan-wedding.comThe GuestsAmplify (Frontend)dasha-tristan-wedding.comThe GuestsAmplify (Frontend)api.dasha-tristan-wedding.comYour CodeEC2 (Django Backend)

3. How to fix your current "Conflict"
Right now, you have your EC2 trying to claim dasha-tristan-wedding.com. If you try to give that same name to Amplify, GoDaddy won't know where to send the traffic—it's like having two houses with the exact same address.

To fix this, do this sequence:

GoDaddy: Change your A Record for @ to point to a new record named api instead.

EC2 Nginx: Update your server_name to api.dasha-tristan-wedding.com.

EC2 Certbot: Run Certbot again for api.dasha-tristan-wedding.com.

Amplify: Now that the root (@) is "free," you can safely add dasha-tristan-wedding.com to Amplify.

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata initial_data.json

# Setup Postgres SQL DB

pip3 install psycopg2-binary