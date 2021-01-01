from django.shortcuts import render
from .models import TodoItems
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.urls import reverse_lazy

# Create your views here.
class TodoHomeView(ListView):
    model = TodoItems
    template_name = 'home.html'

class TodoListView(ListView):
    model= TodoItems


    template_name = 'todolist.html'



class TodoCreate(CreateView):
    model = TodoItems
    template_name = 'todo_new.html'
    fields = '__all__'



class TodoUpdate(UpdateView):
    model = TodoItems
    template_name = 'todo_edit.html'
    fields = ['body','due_date','completed']


class TodoDelete(DeleteView):
    model = TodoItems
    template_name = 'delete.html'
    success_url = reverse_lazy('todo')