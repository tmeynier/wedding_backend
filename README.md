
# Commands

psql -U postgres -d testdb      
\dt
exit
\q

python manage.py createsuperuser
python manage.py runserver

OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES gunicorn backend.wsgi:application --bind 0.0.0.0:8000
python manage.py collectstatic

# Architecture

1. The Backend: AWS App Runner (Django)
2. The Front-end: AWS Amplify (Next.js PWA)