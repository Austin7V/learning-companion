# Learning Companion

A Django-based learning management platform that helps users track learning goals, sessions, and resources with AI-powered summaries.

## Project Overview

Learning Companion helps users:
- Create and manage learning goals (status: planned/in-progress/done)
- Track learning sessions (date, duration, notes, tags)
- Build a resource library (articles, videos, repositories, documents)
- Get AI-powered summaries of sessions (using OpenAI)

## Tech Stack

- **Backend**: Django 4.2
- **Frontend**: Django Templates (HTML/CSS)
- **Database**: SQLite (development)
- **Authentication**: Django built-in auth
- **AI**: OpenAI Chat Completions API
- **Testing**: pytest + pytest-django

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd learning-companion
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

Copy the example environment file and configure it:

```bash
cp .env.example .env
```

Then edit `.env` and add:
- `SECRET_KEY`: Django secret key (generate one if needed)
- `OPENAI_API_KEY`: Your OpenAI API key
- `DEBUG`: Set to `False` for production

### 5. Run Database Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser (Optional)

For accessing Django admin:

```bash
python manage.py createsuperuser
```

### 7. Start Development Server

```bash
python manage.py runserver
```

The app will be available at: `http://localhost:8000/`

## Development

### Running Tests

```bash
pytest
```

With coverage:

```bash
pytest --cov=learning --cov-report=html
```

### Making Model Changes

After modifying models.py:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Django Admin

Access Django admin at: `http://localhost:8000/admin/`

## Project Structure

```
learning-companion/
├── config/              # Django project settings
│   ├── settings.py      # Project configuration
│   ├── urls.py          # Main URL routing
│   └── wsgi.py
├── learning/            # Main Django app
│   ├── models.py        # Database models
│   ├── views.py         # View functions
│   ├── forms.py         # Django forms
│   ├── services.py      # Business logic (AI integration)
│   ├── urls.py          # App URL routing
│   ├── templates/       # HTML templates
│   ├── static/          # CSS, JS, images
│   └── tests.py         # Tests
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
├── .gitignore           # Git ignore file
├── manage.py            # Django management script
└── README.md            # This file
```

## Implementation Status

### Completed
- [x] Project structure
- [x] Django configuration
- [x] Requirements and dependencies
- [x] Environment setup

### In Progress
- [ ] Epic 1: Project Setup (Ticket 1.2, 1.3)
- [ ] Epic 2: Authentication & Profile
- [ ] Epic 3: Goals & Sessions
- [ ] Epic 4: Resources
- [ ] Epic 5: AI Summaries

## Common Commands

```bash
# Start development server
python manage.py runserver

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Django shell
python manage.py shell

# Run tests
pytest

# Run tests with coverage
pytest --cov=learning --cov-report=html

# Django check
python manage.py check

# Collect static files (production)
python manage.py collectstatic
```

## Troubleshooting

### ModuleNotFoundError: No module named 'django'
Make sure virtual environment is activated and dependencies are installed:
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### Database errors
Reset the database:
```bash
rm db.sqlite3
python manage.py migrate
```

### OpenAI API errors
Check that `OPENAI_API_KEY` is set in `.env` file.

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests to ensure nothing breaks
4. Commit with clear message
5. Push to repository

## License

This project is part of a learning program.

---

**Last Updated**: 2026-07-09  
**Version**: 1.0 (MVP)
