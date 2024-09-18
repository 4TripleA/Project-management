from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from register.models import tasks

class adduserform(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class Loginform(forms.Form):  
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Input your password"})) 

# class newprojectform(forms.Form):
#     title = forms.CharField(widget=forms.TextInput(attrs={'class': 'title', 'placeholder': 'Enter title'}))
    
#     class Meta:
#         model = projects
#         fields = "__all__"

class newtaskform(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'title', 'placeholder': 'Enter your project Title'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'body', 'placeholder': 'Enter your Project Description'}))

    class Meta:
        model = tasks
        fields = ("title", "body")



 

