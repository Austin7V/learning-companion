# Learning Companion - MVP Documentation

**Status**: AI Factory Setup Phase  
**Framework**: Django 4.2 + Python 3.9 + Django Templates  
**Project**: Recap Project 6 - Agentic Engineering & AI Factory

---

## 1. Project Overview

**Learning Companion** is a learning management platform that helps users:
- Create and manage learning goals
- Track progress through learning sessions
- Build a library of learning resources
- Get AI-powered session summaries

**Key Characteristics**:
- Django web app with built-in authentication
- SQLite database (development)
- Django templates for UI (no React/Vue)
- OpenAI API for summaries
- Simple, practical MVP approach

---

## 2. Architecture

### 2.1 Tech Stack
- **Backend**: Django 4.2
- **Frontend**: Django Templates (HTML/CSS)
- **Database**: SQLite (development)
- **Authentication**: Django built-in auth (User model)
- **AI Integration**: OpenAI Chat Completions API
- **No**: JWT, React, Redux, REST API, PostgreSQL (for MVP)

### 2.2 Core Components

```
learning-companion/
├── config/              # Django project configuration
│   ├── settings.py      # Project settings
│   ├── urls.py          # URL routing
│   └── wsgi.py
├── learning/            # Main app
│   ├── models.py        # Core data models
│   ├── views.py         # View functions (not API)
│   ├── forms.py         # Django forms
│   ├── services.py      # AI service (OpenAI)
│   ├── urls.py          # App URL routing
│   ├── templates/       # HTML templates
│   │   └── learning/
│   │       ├── base.html
│   │       ├── dashboard.html
│   │       ├── goal_list.html
│   │       ├── goal_detail.html
│   │       ├── session_form.html
│   │       ├── resource_list.html
│   │       └── ...
│   ├── static/          # CSS, JS, images
│   │   └── css/
│   │       └── style.css
│   └── tests.py         # Tests
├── db.sqlite3           # SQLite database
└── README.md            # Project documentation
```

### 2.3 Database Models

**Core Models**:
- `Profile` - User profile (name, cohort, focus_area)
- `Goal` - Learning goals (title, status: planned/in-progress/done, deadline)
- `LearningSession` - Study sessions (date, duration_minutes, notes, tags)
- `Resource` - Learning resources (type: article/video/repo/doc, url, title)
- `SessionResource` - Link sessions to resources
- `Summary` - AI-generated summaries (linked to sessions)

---

## 3. Pipeline Stages & AI Factory Configuration

### Stage 1: RESEARCH
**Purpose**: Understand requirements, analyze codebase, gather context.

**SKILLS**:
- `Explore` - Fast code exploration (search by pattern, grep symbols)
- `deep-research` - Multi-source web research with fact-checking

**RULES**:
- Always run `git status` before analyzing code
- Use Explore agent for broad codebase searches (>3 queries)
- Prioritize reading core files: `models.py`, `settings.py`, `views.py`, `forms.py`
- Document assumptions in task comments
- Focus on Django conventions, not REST/API patterns

**HOOKS** (settings.json):
```json
{
  "hooks": [
    {
      "event": "before_implementation",
      "command": "python manage.py check",
      "description": "Validate Django project structure"
    }
  ]
}
```

---

### Stage 2: PLANNING
**Purpose**: Design solution architecture, break down tasks, validate approach.

**SKILLS**:
- `Plan` - Software architect for step-by-step implementation plans
- `artifact-design` - For UI/UX planning of new features
- `dataviz` - For designing data visualization components

**RULES**:
- Create detailed implementation plan before coding
- Identify critical files and dependencies
- Consider backward compatibility
- Document all external API integrations
- Prefer composition over inheritance
- Use EnterPlanMode for major features (auth, AI integration, etc.)

**HOOKS** (settings.json):
```json
{
  "hooks": [
    {
      "event": "before_coding",
      "command": "find . -name '*.py' ! -path './.venv/*' | xargs pylint --fail-under=7.0 2>/dev/null || true",
      "description": "Check code quality before implementation"
    }
  ]
}
```

---

### Stage 3: IMPLEMENTATION
**Purpose**: Write code following architecture and Django best practices.

**SKILLS**:
- `run` - Launch and drive the app to verify changes work
- `verify` - End-to-end verification of feature implementation
- `code-review` - Review changes for correctness before commit

**RULES**:
- Follow Django naming conventions and structure
- Use Django built-in auth (User model)
- Keep models simple and focused
- Use Django ORM instead of raw SQL
- Write migrations for all model changes
- No hardcoded values, use settings.py for configuration
- Use Django forms for all user input validation
- OpenAI API calls must be wrapped in error handlers
- Use Django templates for all views
- No REST API - use traditional view functions with templates

**HOOKS** (settings.json):
```json
{
  "hooks": [
    {
      "event": "after_model_change",
      "command": "python manage.py makemigrations && python manage.py showmigrations",
      "description": "Auto-generate migrations"
    },
    {
      "event": "before_commit",
      "command": "python -m pytest --cov=learning --cov-fail-under=70 2>/dev/null || true",
      "description": "Run tests before commit"
    }
  ]
}
```

---

### Stage 4: TESTING
**Purpose**: Verify functionality, integration, and edge cases.

**SKILLS**:
- `verify` - Drive features end-to-end in the real app
- `code-review` - Test coverage and quality assessment

**RULES**:
- Write unit tests for all business logic (services)
- Write integration tests for API endpoints
- Test error scenarios and edge cases
- Mock external API calls (Claude API) in tests
- Test data migrations and schema changes
- Use Django test client for API testing
- Maintain 70%+ code coverage

**HOOKS** (settings.json):
```json
{
  "hooks": [
    {
      "event": "run_tests",
      "command": "python manage.py test learning --verbosity=2 --failfast",
      "description": "Run all tests"
    },
    {
      "event": "test_coverage",
      "command": "coverage run --source='learning' manage.py test learning && coverage report --fail-under=70",
      "description": "Test coverage check"
    }
  ]
}
```

---

### Stage 5: REVIEW
**Purpose**: Quality assurance, security review, code standards.

**SKILLS**:
- `code-review` - Find bugs, verify correctness
- `security-review` - Security vulnerability assessment
- `simplify` - Refactoring and code cleanup

**RULES**:
- All changes must pass `pylint` and `black` formatting
- Security review required for: auth, API, AI integration, user data
- Database migrations reviewed for schema consistency
- API changes documented in docstrings
- No direct SQL queries (use Django ORM)
- No secrets in code (use environment variables)

**HOOKS** (settings.json):
```json
{
  "hooks": [
    {
      "event": "before_push",
      "command": "black --check . && pylint learning --fail-under=7.0 2>/dev/null || true",
      "description": "Code style and quality check"
    }
  ]
}
```

---

## 4. GitHub Project Board - Tickets Summary

See TICKETS.md for full ticket details.

### Epic 1: Project Setup (3 tickets)
- Setup project structure & requirements.txt
- Setup OpenAI API integration
- Create basic Django views & templates

### Epic 2: Authentication & Profile (2 tickets)
- User registration/login (Django built-in auth)
- User Profile model (name, cohort, focus_area)

### Epic 3: Goals & Sessions (3 tickets)
- Goal model (title, status: planned/in-progress/done)
- Learning Session model (date, duration, notes, tags)
- Goal list/detail views with forms

### Epic 4: Resources (2 tickets)
- Resource model (type: article/video/repo/doc)
- Resource list view with simple search

### Epic 5: AI Summaries (1 ticket)
- OpenAI integration for session summaries
- Summary view and caching

### Total: 11 tickets across 5 epics (simplified MVP)

---

## 5. Coding Standards & Conventions

### Python/Django
- Follow PEP 8 with `black` for formatting
- Use type hints for all functions
- Docstrings: One-liner for simple functions, full docs for complex logic
- Model naming: CamelCase, singular (User, Goal, LearningSession)
- View/serializer naming: Clear verbs (ListGoals, CreateGoal, etc.)

### Git Workflow
- Feature branches: `feature/<feature-name>`
- Bug fixes: `fix/<bug-description>`
- Commits: Conventional commits format
  - `feat: add goal creation endpoint`
  - `fix: handle null values in session summary`
  - `test: add tests for AI service`
  - `docs: update API documentation`

### View & URL Design
- Function-based views (not class-based, keep it simple)
- URL patterns: `/learning/goals/`, `/learning/sessions/`, `/learning/resources/`
- Use Django forms for POST/PUT handling
- Redirect after POST (PRG pattern)
- Use Django messages framework for user feedback

### Testing
- Unit tests in `tests/` directory
- Use `pytest` with fixtures
- Mock external APIs (Claude SDK)
- Minimum 70% coverage
- Test naming: `test_<feature>_<scenario>`

---

## 6. AI Integration Strategy

### OpenAI Chat Completions API Usage
- **Summaries**: Condense learning session notes into key points (MVP feature)
- No recommendations or content generation in MVP

### Best Practices
- Use openai package for API calls
- Wrap API calls with error handling (timeout, API errors)
- Store summaries in database to avoid re-generation
- Log all API calls for debugging
- Use environment variables for API key (OPENAI_API_KEY)
- Handle API errors gracefully (show user-friendly messages)

### Simple Implementation
- Basic prompt: "Summarize these learning session notes in 3-5 bullets"
- Cache generated summaries in Summary model
- No rate limiting needed for MVP
- Basic error messages: "Summary generation failed, please try again"

---

## 7. Dependency Management

### Production Stack
```
Django==4.2.30
openai>=1.0.0                        # OpenAI API client
python-dotenv==1.0.0                 # Environment variables
```

### Development
```
pytest==7.4.0
pytest-django==4.5.2
pytest-cov==4.1.0
```

---

## 8. Implementation Checklist (MVP)

- [ ] Setup project structure & dependencies (Ticket 1.1)
- [ ] Setup OpenAI API integration (Ticket 1.2)
- [ ] Create Django templates & base setup (Ticket 1.3)
- [ ] User registration/login (Ticket 2.1)
- [ ] User Profile model & edit (Ticket 2.2)
- [ ] Goal model & CRUD views (Ticket 3.1)
- [ ] Learning Session model & views (Ticket 3.2)
- [ ] Dashboard with overview (Ticket 3.3)
- [ ] Resource model & list (Ticket 4.1)
- [ ] Session resource linking (Ticket 4.2)
- [ ] AI summaries (OpenAI) (Ticket 5.1)
- [ ] Write tests for all features
- [ ] MVP complete and working

---

## 9. Quick Start Commands

```bash
# Initial setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Create .env file from .env.example
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# Database setup
python manage.py migrate

# Create superuser (for admin)
python manage.py createsuperuser

# Development server
python manage.py runserver

# Testing
pytest
pytest --cov=learning --cov-report=html

# Making changes to models
python manage.py makemigrations
python manage.py migrate
```

---

## 10. Contact & Escalation

- **Issues**: Create GitHub issues in this project
- **Questions about implementation**: Review CLAUDE.md pipeline stages
- **Questions about AI features**: Check AI Integration Strategy section
- **Security concerns**: Contact project maintainer directly

---

**Last Updated**: 2026-07-09  
**Version**: 1.0 - Initial AI Factory Setup
