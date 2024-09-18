from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django. contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from register.forms import adduserform, newtaskform
from django.contrib import messages
from register.models import tasks
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def home(request):
    return render(request, "home.html", {'posts': tasks.objects.all().order_by('-date_assigned')})

def master(request):
    return render(request, "master.html", {})

def register(request):
    submitted = False
    if request.method == "POST":

        form = adduserform(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Registration Successful')

            return redirect('login')
    else:
        form = adduserform
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "Register.html", {'form':form, 'submitted':submitted})


def taskss(request):
    user = request.user.id

    if request.method == "POST":
        form = newtaskform(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            body = form.cleaned_data.get('body')
            q, created = tasks.objects.get_or_create(title=title, body=body)
            q.save()

        return redirect("tasksss")
    else:
        form = newtaskform()
    return render(request, "newtasks.html", {'form': form})

def taskview(request):
    return render(request, "tasks.html", {'posts': tasks.objects.all().order_by('-date_assigned')})
    

def logout(request):
    return render(request, "registration/logout.html", {})



