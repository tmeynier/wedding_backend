
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

# Architecture

1. The Backend: AWS App Runner (Django)
2. The Front-end: AWS Amplify (Next.js PWA)

1. The Architecture
Database: AWS RDS (PostgreSQL) — Managed database service.

Backend: AWS App Runner — Connects to your GitHub, builds a container, and runs your Django API.

Frontend: AWS Amplify Hosting — Connects to your GitHub, builds your Next.js app, and serves it via a global CDN.

2. Step-by-Step Deployment
Phase A: Setup the Database (RDS)
Before the backend can run, it needs a place to store data.

Search for RDS in the AWS Console.

Create Database: Select Standard Create > PostgreSQL.

Template: Choose Free Tier (to stay within low/no cost).

Settings: Set your DB Instance Identifier, Master Username, and Password. Save these!

Connectivity:

Set Public Access to No (for security).

Create a new VPC Security Group (name it rds-sg).

Once created, copy the Endpoint string (looks like ...rds.amazonaws.com).

Phase B: Deploy Django (App Runner)
App Runner makes scaling easy.

Search for App Runner > Create Service.

Source: Select Source code repository and connect your GitHub. Select your repo and branch.

Build Settings:

Runtime: Python 3.

Build command: pip install -r requirements.txt

Start command: gunicorn backend.wsgi:application --bind 0.0.0.0:8080 (ensure gunicorn is in your requirements.txt).

Environment Variables: Add your DB_NAME, DB_USER, DB_PASSWORD, DB_HOST (the RDS endpoint), and DJANGO_SETTINGS_MODULE.

Networking: You will need to create a VPC Connector in the App Runner settings so it can "talk" to the private RDS database.

Phase C: Deploy Next.js (Amplify)
Search for AWS Amplify > New App > Host web app.

Connect your GitHub and select the frontend repository.

Build settings: Amplify usually auto-detects Next.js. Ensure the baseDirectory is set to .next.

Environment Variables: Add a variable NEXT_PUBLIC_API_URL and set it to your App Runner URL (e.g., https://abc123xyz.us-east-1.awsapprunner.com/api).

Click Save and Deploy.

3. Crucial Configuration Changes
To make this work in the cloud, you must update your local code:

Django settings.py (Production ready)
Python
import os

# DO NOT keep secrets in code. Use Environment Variables on AWS.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'fallback-key')
DEBUG = False 

# Allow App Runner and Amplify to talk to you
ALLOWED_HOSTS = ['.awsapprunner.com', 'your-amplify-app.com']

# Update CORS to allow your Amplify URL
CORS_ALLOWED_ORIGINS = [
    "https://main.d123456.amplifyapp.com", # Your actual Amplify URL
]
Next.js Fetching
Update your index.tsx to use the environment variable:

TypeScript
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

useEffect(() => {
    fetch(`${API_URL}/items/`)
      .then(res => res.json())
      .then(data => setItems(data));
}, []);
4. The "Final Boss": Security Groups
You must tell the Database to let the Backend in:

Go to the RDS Console > Select your DB.

Click on the Security Group (rds-sg).

Edit Inbound Rules: Add a rule for Type: PostgreSQL (5432) and for the Source, select the Security Group assigned to your App Runner service.

Would you like me to help you create the Dockerfile for your Django app? (This is often more reliable for App Runner than using the raw Python runtime).