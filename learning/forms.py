from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Goal, LearningSession, Resource


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'cohort', 'focus_area')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'cohort': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cohort (optional)'}),
            'focus_area': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Focus Area (optional)', 'rows': 3}),
        }


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ('title', 'description', 'status', 'deadline')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Goal Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description (optional)', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class LearningSessionForm(forms.ModelForm):
    class Meta:
        model = LearningSession
        fields = ('title', 'goal', 'date', 'duration_minutes', 'notes', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Session Title'}),
            'goal': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'duration_minutes': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration (minutes)', 'min': '1'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Session notes...', 'rows': 4}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tags (comma-separated)'}),
        }


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ('url', 'title', 'type', 'description')
        widgets = {
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Resource Title'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description (optional)', 'rows': 4}),
        }
