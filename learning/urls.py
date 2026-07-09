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
    # Dashboard
    path('', views.dashboard, name='dashboard'),
]
