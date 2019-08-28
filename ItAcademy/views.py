from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def home(request):
    context = {}
    return render(request, 'home.html', context)


def login(request):
    context ={}
    return render(request, 'login.html', context)
