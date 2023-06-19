from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Todo
from core.forms import TodoForm

# Create your views here.


def home(request) :
  form = TodoForm()
  todos = Todo.objects.all()
  if request.method == 'POST' :
    form = TodoForm(request.POST)
    if form.is_valid :
      form.save()
      return redirect('home')
  return render(request,"home.html", {'form': form ,'todos':todos})


def update(request, todo_id) :
  todo = Todo.objects.get(id=todo_id)  # here we get the id of required todo to update
  form = TodoForm(instance=todo)
  if request.method == 'POST' :
    form = TodoForm(request.POST , instance=todo) # updated data and previous data
    if form.is_valid() :
      form.save()
      return redirect('home')
  return render(request, 'update.html' ,{'form':form})

def delete(request, todo_id):
  if request.method == 'POST' :
    Todo.objects.get(id=todo_id).delete()
    return redirect("home")