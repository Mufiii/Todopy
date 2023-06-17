from django.shortcuts import render
from django.http import HttpResponse
from core.forms import TodoForm

# Create your views here.


def home(request) :
  form = TodoForm()
  return render(request,"home.html", {'form': form})