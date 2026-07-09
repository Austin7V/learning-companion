# GitHub Project Board - MVP Tickets

## Epic 1: Project Setup (3 tickets)

### Issue 1.1: Setup Project Structure & Dependencies
```
Title: Setup project structure and requirements.txt
Labels: epic/setup, priority/high, type/setup
Description:
- Create requirements.txt with dependencies:
  * Django==4.2.30
  * openai>=1.0.0
  * python-dotenv==1.0.0
  * pytest==7.4.0
  * pytest-django==4.5.2
- Create .env.example with:
  * SECRET_KEY=your-secret-key
  * OPENAI_API_KEY=your-api-key
  * DEBUG=True
- Create .gitignore for Django
- Create README.md with setup instructions
- Run: pip install -r requirements.txt && python manage.py migrate

Acceptance Criteria:
- requirements.txt exists with all dependencies
- .env.example template exists
- python manage.py runserver works without errors
- python manage.py check passes
- .gitignore excludes .env, *.pyc, __pycache__, db.sqlite3
```

### Issue 1.2: Setup OpenAI API Integration
```
Title: Create OpenAI API service
Labels: epic/setup, ai-integration, priority/high, type/feature
Description:
- Create learning/services.py with:
  * OpenAI client initialization from .env
  * get_summary(notes: str) function
  * Error handling for API failures
  * Logging for all API calls
- Function takes session notes and returns summary (3-5 bullets)
- Handle API errors: show user-friendly messages
- Don't regenerate summaries (check if exists in DB first)

Acceptance Criteria:
- OpenAI client configured with API key from .env
- Summary function returns concise bullet points
- API errors handled gracefully (try/except with logging)
- Can be tested with mock (monkeypatch)
```

### Issue 1.3: Create Django Templates & Base Setup
```
Title: Create base.html and initial templates
Labels: epic/setup, priority/medium, type/feature
Description:
- Create learning/templates/learning/base.html:
  * Navigation bar with Home, Goals, Sessions, Resources, Logout links
  * User display ({{ user.username }})
  * Bootstrap 5 for styling
  * CSS file at static/css/style.css
- Create initial views.py with:
  * dashboard view (just "Welcome" for now)
  * @login_required decorators where needed
- Create learning/urls.py with base patterns
- Create config/urls.py to include learning.urls

Acceptance Criteria:
- Base template renders with navigation
- CSS file loads correctly
- Login required decorator works
- All pages show user is authenticated
```

---

## Epic 2: Authentication & Profile (2 tickets)

### Issue 2.1: User Registration & Login
```
Title: Implement user registration and login
Labels: epic/auth, priority/high, type/feature
Description:
- Create learning/forms.py with:
  * RegisterForm (username, email, password)
  * Simple form validation
- Create views:
  * register view (GET: show form, POST: create user)
  * login view (use Django auth)
  * logout view
- Create templates:
  * learning/register.html
  * learning/login.html (use Django auth login)
- Add forms to base.html navbar (Login/Register or Logout)
- Create learning/models.py with Profile model:
  * name (CharField, max_length=200)
  * cohort (CharField, max_length=100, blank=True)
  * focus_area (TextField, blank=True)
  * linked to User 1:1

Acceptance Criteria:
- Users can register with valid email/username
- Users can login with credentials
- Users can logout
- Profile model created (migration created)
- New users have Profile created automatically (use signals)
```

### Issue 2.2: User Profile View & Edit
```
Title: Create profile view and edit form
Labels: epic/auth, priority/medium, type/feature
Description:
- Create ProfileForm in forms.py (name, cohort, focus_area)
- Create views:
  * profile_view (GET: show profile, POST: update)
  * profile_detail view (read-only, show name/cohort/focus_area)
- Create templates:
  * learning/profile.html (edit form)
  * learning/profile_detail.html (view)
- Add Profile link to navigation bar
- Show cohort and focus_area on profile

Acceptance Criteria:
- Users can view own profile
- Users can edit name, cohort, focus_area
- Profile updates save correctly
- Changes reflected immediately
```

---

## Epic 3: Goals & Sessions (3 tickets)

### Issue 3.1: Goal Model & CRUD Views
```
Title: Create Goal model and list/create views
Labels: epic/core, priority/high, type/feature
Description:
- Create Goal model in models.py:
  * title (CharField)
  * description (TextField, blank=True)
  * status (CharField, choices: planned/in-progress/done)
  * deadline (DateField, blank=True, null=True)
  * owner (ForeignKey to User)
  * created_at (DateTimeField, auto_now_add)
  * updated_at (DateTimeField, auto_now)
- Create GoalForm in forms.py (title, description, status, deadline)
- Create views:
  * goal_list: shows user's goals, filter by status
  * goal_detail: show single goal
  * goal_create: form to create goal
  * goal_update: form to edit goal
  * goal_delete: delete goal (with confirmation)
- Create templates:
  * learning/goal_list.html (table of goals)
  * learning/goal_detail.html (show goal, sessions count)
  * learning/goal_form.html (create/edit form)
- Add URLs to learning/urls.py
- Add Goals link to navigation

Acceptance Criteria:
- Users see only their own goals
- Can create goals with required fields
- Can update goal status
- Can delete goals
- Status filtering works (planned/in-progress/done)
- Templates show all relevant fields
```

### Issue 3.2: Learning Session Model & CRUD Views
```
Title: Create LearningSession model and views
Labels: epic/core, priority/high, type/feature
Description:
- Create LearningSession model:
  * title (CharField)
  * goal (ForeignKey to Goal, blank=True, null=True)
  * date (DateField)
  * duration_minutes (IntegerField)
  * notes (TextField)
  * tags (CharField, max_length=500, blank=True, comma-separated)
  * owner (ForeignKey to User)
  * created_at (DateTimeField, auto_now_add)
  * updated_at (DateTimeField, auto_now)
- Create SessionForm in forms.py (all fields above)
- Create views:
  * session_list: show user's sessions (newest first)
  * session_detail: show single session (with summary if exists)
  * session_create: form to create session
  * session_update: form to edit session
  * session_delete: delete session
- Create templates:
  * learning/session_list.html (table of sessions)
  * learning/session_detail.html (show session, links to generate summary)
  * learning/session_form.html (create/edit form)
- Add Sessions link to navigation

Acceptance Criteria:
- Users see only their own sessions
- Can create sessions with date, duration, notes
- Can filter/sort sessions (by date, goal, etc.)
- Tags display correctly
- Links to Goal work (if linked)
- Can update and delete sessions
```

### Issue 3.3: Dashboard with Goals & Sessions Overview
```
Title: Create user dashboard
Labels: epic/core, priority/medium, type/feature
Description:
- Create dashboard view:
  * Show count: active goals, completed sessions, total hours
  * Show recent 5 sessions (table)
  * Show active goals (status != done)
  * Quick links to create goal/session
- Create dashboard.html template:
  * Stats cards (goals count, sessions count, total hours)
  * Recent sessions section
  * Active goals section
- Set dashboard as home page (after login)
- Add /learning/ as home view

Acceptance Criteria:
- Dashboard shows accurate counts
- Recent sessions display correctly
- Active goals display correctly
- Quick action buttons work
- Responsive layout
```

---

## Epic 4: Resources (2 tickets)

### Issue 4.1: Resource Model & List View
```
Title: Create Resource model and list view
Labels: epic/resources, priority/high, type/feature
Description:
- Create Resource model:
  * url (URLField)
  * title (CharField)
  * type (CharField, choices: article/video/repo/doc)
  * description (TextField, blank=True)
  * added_by (ForeignKey to User)
  * created_at (DateTimeField, auto_now_add)
- Create ResourceForm in forms.py
- Create views:
  * resource_list: show all resources, filter by type
  * resource_detail: show single resource
  * resource_create: form to add resource
  * resource_delete: delete own resources
- Create templates:
  * learning/resource_list.html (table with type icons)
  * learning/resource_detail.html
  * learning/resource_form.html
- Add Resources link to navigation
- Add icons/colors for each type (article/video/repo/doc)

Acceptance Criteria:
- Users can browse all resources (created by any user)
- Can filter by type
- Can create new resources
- Can delete own resources
- Resource links work and open correctly
- Type filtering works
```

### Issue 4.2: Session Resource Linking
```
Title: Link resources to learning sessions
Labels: epic/resources, priority/medium, type/feature
Description:
- Create SessionResource model:
  * session (ForeignKey to LearningSession)
  * resource (ForeignKey to Resource)
  * created_at (DateTimeField, auto_now_add)
- Update SessionForm to allow selecting resources (M2M or FK list)
- Update session_detail template:
  * Show linked resources with links
  * Allow adding/removing resources from session
- Update session_form template:
  * Show available resources (checkboxes)
  * Allow selecting multiple resources
- Add "Add Resource" functionality on session detail

Acceptance Criteria:
- Can link resources when creating sessions
- Can link resources to existing sessions
- Session detail shows linked resources
- Can unlink resources
- Removing resource doesn't delete it (just unlinks)
```

---

## Epic 5: AI Summaries (1 ticket)

### Issue 5.1: Generate AI Summaries for Sessions
```
Title: OpenAI integration for session summaries
Labels: epic/ai, priority/high, type/feature
Description:
- Create Summary model:
  * session (OneToOneField to LearningSession)
  * summary_text (TextField)
  * created_at (DateTimeField, auto_now_add)
- Create generate_summary view:
  * POST endpoint on session_detail page
  * Calls learning/services.py get_summary(notes)
  * Saves to Summary model
  * Redirects back to session_detail
- Update session_detail template:
  * Show summary if exists
  * Show "Generate Summary" button if doesn't exist
  * Show generated date
- Add error handling:
  * Show user message if API fails
  * Use Django messages framework
- Add simple caching:
  * Check if Summary exists before calling API
  * Show cached summary if available

Acceptance Criteria:
- Users can request summary generation
- OpenAI API is called with session notes
- Summary displays as 3-5 bullets
- Cached summaries don't re-call API
- Errors handled gracefully
- User sees feedback (success or error message)
```

---

## How to Use These Tickets

### Creating Issues in GitHub

Copy ticket content into GitHub issue:
1. Go to GitHub repo Issues tab
2. Create New Issue
3. Copy Title and Description
4. Add Labels
5. Click Create Issue

Or use GitHub CLI:
```bash
gh issue create --title "Setup project structure..." \
  --body "See TICKETS.md Issue 1.1" \
  --label "epic/setup,priority/high"
```

### Project Board Setup

1. Create GitHub Project Board: "Learning Companion MVP"
2. Add columns: Backlog, In Progress, Review, Done
3. Set up automation (optional):
   - Moved to "In Progress" when assigned
   - Moved to "Done" when closed
4. Add all issues to board

### Tracking Progress

- Move tickets from Backlog → In Progress → Review → Done
- Link PRs to issues
- Close issue when PR merged

---

**Total Tickets**: 11  
**Total Epics**: 5  
**Estimated Time**: 2-3 weeks for one developer  
**MVP Focus**: Simple, practical, no complex features

---

## Epic Breakdown

| Epic | Tickets | Priority | Est. Time |
|------|---------|----------|-----------|
| Setup | 3 | HIGH | 1 week |
| Auth | 2 | HIGH | 3 days |
| Core | 3 | HIGH | 1 week |
| Resources | 2 | MEDIUM | 3 days |
| AI | 1 | HIGH | 2 days |
| **Total** | **11** | - | **2-3 weeks** |

---

**Last Updated**: 2026-07-09  
**Project**: Learning Companion MVP  
**Status**: Ready for implementation
