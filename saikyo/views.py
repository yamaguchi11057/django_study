from django.shortcuts import render
from .models import TodoModel
from django.views.generic import ListView, DetailView

# Create your views here.
class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel