
# Commands

psql -U postgres -d testdb      
\dt
exit
\q

python manage.py createsuperuser
python manage.py runserver

# Architecture

1. The Backend: AWS App Runner (Django)
2. The Front-end: AWS Amplify (Next.js PWA)