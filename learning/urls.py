from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Profile
    path('profile/', views.profile_detail, name='profile_detail'),
    path('profile/edit/', views.profile_view, name='profile_view'),
    # Goals
    path('goals/', views.goal_list, name='goal_list'),
    path('goals/new/', views.goal_create, name='goal_create'),
    path('goals/<int:pk>/', views.goal_detail, name='goal_detail'),
    path('goals/<int:pk>/edit/', views.goal_update, name='goal_update'),
    path('goals/<int:pk>/delete/', views.goal_delete, name='goal_delete'),
    # Sessions
    path('sessions/', views.session_list, name='session_list'),
    path('sessions/new/', views.session_create, name='session_create'),
    path('sessions/<int:pk>/', views.session_detail, name='session_detail'),
    path('sessions/<int:pk>/edit/', views.session_update, name='session_update'),
    path('sessions/<int:pk>/delete/', views.session_delete, name='session_delete'),
    # Dashboard
    path('', views.dashboard, name='dashboard'),
]
