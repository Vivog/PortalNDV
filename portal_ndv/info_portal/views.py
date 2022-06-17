from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, CreateView, DetailView
from slugify import slugify

from .forms import *
from .models import *


# Create your views here.

def home(request):
    # num_divisions = Divisions.objects.all().count()
    # num_staff = Staff.objects.all().count()
    # num_doc = Documents.objects.all().count()
    # context = {
    #     'num_divisions': num_divisions,
    #     'num_staff': num_staff,
    #     'num_doc': num_doc}
    # return render(request, 'nio_app/home.html', context=context)
    return render(request, 'info_portal/index.html')


