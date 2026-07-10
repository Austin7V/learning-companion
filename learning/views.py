from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.db.models import Q, Sum
from datetime import datetime
from .forms import RegisterForm, ProfileForm, GoalForm, LearningSessionForm
from .models import Profile, Goal, LearningSession


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! You can now login.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'learning/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'learning/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


@login_required
def profile_view(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile_detail')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'learning/profile.html', {'form': form, 'profile': profile})


@login_required
def profile_detail(request):
    profile = request.user.profile
    return render(request, 'learning/profile_detail.html', {'profile': profile})


@login_required
def goal_list(request):
    status_filter = request.GET.get('status', '')
    goals = Goal.objects.filter(owner=request.user)

    if status_filter:
        goals = goals.filter(status=status_filter)

    context = {
        'goals': goals,
        'status_choices': Goal.STATUS_CHOICES,
        'selected_status': status_filter,
    }
    return render(request, 'learning/goal_list.html', context)


@login_required
def goal_detail(request, pk):
    goal = get_object_or_404(Goal, pk=pk, owner=request.user)
    return render(request, 'learning/goal_detail.html', {'goal': goal})


@login_required
def goal_create(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.owner = request.user
            goal.save()
            messages.success(request, 'Goal created successfully!')
            return redirect('goal_detail', pk=goal.pk)
    else:
        form = GoalForm()

    return render(request, 'learning/goal_form.html', {'form': form, 'title': 'Create New Goal'})


@login_required
def goal_update(request, pk):
    goal = get_object_or_404(Goal, pk=pk, owner=request.user)

    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Goal updated successfully!')
            return redirect('goal_detail', pk=goal.pk)
    else:
        form = GoalForm(instance=goal)

    return render(request, 'learning/goal_form.html', {'form': form, 'goal': goal, 'title': 'Edit Goal'})


@login_required
def goal_delete(request, pk):
    goal = get_object_or_404(Goal, pk=pk, owner=request.user)

    if request.method == 'POST':
        goal.delete()
        messages.success(request, 'Goal deleted successfully!')
        return redirect('goal_list')

    return render(request, 'learning/goal_confirm_delete.html', {'goal': goal})


@login_required
def session_list(request):
    goal_filter = request.GET.get('goal', '')
    sessions = LearningSession.objects.filter(owner=request.user)

    if goal_filter:
        sessions = sessions.filter(goal__id=goal_filter)

    context = {
        'sessions': sessions,
        'goals': Goal.objects.filter(owner=request.user),
        'selected_goal': goal_filter,
    }
    return render(request, 'learning/session_list.html', context)


@login_required
def session_detail(request, pk):
    session = get_object_or_404(LearningSession, pk=pk, owner=request.user)
    return render(request, 'learning/session_detail.html', {'session': session})


@login_required
def session_create(request):
    if request.method == 'POST':
        form = LearningSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.owner = request.user
            session.save()
            messages.success(request, 'Learning session created successfully!')
            return redirect('session_detail', pk=session.pk)
    else:
        form = LearningSessionForm()
        # Filter goals to only show user's goals
        form.fields['goal'].queryset = Goal.objects.filter(owner=request.user)

    return render(request, 'learning/session_form.html', {'form': form, 'title': 'Create New Session'})


@login_required
def session_update(request, pk):
    session = get_object_or_404(LearningSession, pk=pk, owner=request.user)

    if request.method == 'POST':
        form = LearningSessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            messages.success(request, 'Learning session updated successfully!')
            return redirect('session_detail', pk=session.pk)
    else:
        form = LearningSessionForm(instance=session)
        form.fields['goal'].queryset = Goal.objects.filter(owner=request.user)

    return render(request, 'learning/session_form.html', {'form': form, 'session': session, 'title': 'Edit Session'})


@login_required
def session_delete(request, pk):
    session = get_object_or_404(LearningSession, pk=pk, owner=request.user)

    if request.method == 'POST':
        session.delete()
        messages.success(request, 'Learning session deleted successfully!')
        return redirect('session_list')

    return render(request, 'learning/session_confirm_delete.html', {'session': session})


@login_required
def dashboard(request):
    user = request.user

    # Stats
    active_goals_count = Goal.objects.filter(owner=user, status__in=['planned', 'in-progress']).count()
    completed_sessions_count = LearningSession.objects.filter(owner=user).count()
    total_hours_result = LearningSession.objects.filter(owner=user).aggregate(total_minutes=Sum('duration_minutes'))
    total_minutes = total_hours_result['total_minutes'] or 0
    total_hours = round(total_minutes / 60, 1)

    # Recent sessions (5 most recent)
    recent_sessions = LearningSession.objects.filter(owner=user).order_by('-date')[:5]

    # Active goals (not done)
    active_goals = Goal.objects.filter(owner=user, status__in=['planned', 'in-progress']).order_by('-created_at')

    context = {
        'active_goals_count': active_goals_count,
        'completed_sessions_count': completed_sessions_count,
        'total_hours': total_hours,
        'recent_sessions': recent_sessions,
        'active_goals': active_goals,
    }
    return render(request, 'learning/dashboard.html', context)
