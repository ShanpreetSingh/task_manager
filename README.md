# Task Manager - Django 
A Django project with REST API, authentication, Celery background tasks, and Telegram bot integration.
## Features
✅ Public and protected API endpoints  
✅ Token & session authentication  
✅ User registration with email notification  
✅ Telegram bot integration  
✅ Celery background tasks  
✅ PostgreSQL/SQLite support  
✅ Environment variables configuration  
✅ Docker-ready setup  
## Setup Instructions

### Prerequisites
- Python 3.10+
- PostgreSQL (optional)
- Redis (for Celery)
- Telegram bot token
### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ShanpreetSingh/task_manager.git
   cd task_manager
2. Create and activate virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    .\venv\Scripts\activate  # Windows
3.Install dependencies:

    pip install -r requirements.txt
4. Configure environment:
     ```bash
    cp .env.example .env
Edit .env with your settings.

    
     



### Database Setup


Option 1: SQLite (Default)

No additional setup required


  Option 2: PostgreSQL


Create database:


                  
    psql -U postgres -c "CREATE DATABASE taskmanager;"


Update .env:

      
      DB_ENGINE=django.db.backends.postgresql

      DB_NAME=taskmanager

      DB_USER=postgres

      DB_PASSWORD=yourpassword

      DB_HOST=localhost

      DB_PORT=5432
  ### Running the Project
1. Apply migrations:

           python manage.py migrate
2. Create superuser:

           python manage.py createsuperuser
3. Run development server:
         
           python manage.py runserver

4. Start Celery worker (in new terminal):
           
           celery -A task_manager worker --loglevel=info
5. Telegram bot starts automatically with Django
### API Documentation

Authentication

POST /api-token-auth/ - Get auth token

POST /api/register/ - Register new user

GET /login/ - Web login page

API Endpoints

GET /api/public/ - Public endpoint (no auth)

GET /api/protected/ - Protected endpoint (requires auth)

GET /api/telegram-users/ - List registered Telegram users (admin)

Telegram Bot

Send /start to your bot to register
## Environment Variables
  ```
# Django Configuration
DEBUG=False
SECRET_KEY=your-secure-secret-key-here  # Generate with: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Database Settings (PostgreSQL example)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=taskmanager
DB_USER=postgres
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432

# Redis/Celery Configuration
REDIS_URL=redis://localhost:6379/0

# Telegram Integration
TELEGRAM_BOT_TOKEN=your-telegram-bot-token  # Get from @BotFather

# Security Settings (Production)
ALLOWED_HOSTS=localhost,127.0.0.1  # Comma-separated list
CSRF_TRUSTED_ORIGINS=http://localhost,http://127.0.0.1

# Email Configuration (Example for development)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
DEFAULT_FROM_EMAIL=admin@taskmanager.com
```
### Project Structure

```
task_manager/
├── .env.example       # Environment template
├── manage.py          # Django CLI
├── task_manager/      # Project config
│   ├── settings.py    # Main settings
│   ├── celery.py      # Celery config
│   └── urls.py        # Root URLs
├── users/             # Custom app
│   ├── models.py      # Database models
│   ├── views.py       # API views  
│   ├── tasks.py       # Celery tasks
│   └── telegram_bot.py # Bot handler
└── templates/         # HTML templates
 ```


### Deployment


With Docker
    
          docker-compose up --build

Production Notes

Set DEBUG=False

Configure proper ALLOWED_HOSTS

Use proper database credentials

Set up HTTPS
## Developed By:



Shanpreet Singh