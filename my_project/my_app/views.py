from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Todo

class TodoListView(ListView):
    model = Todo
    template_name = "todo_list.html"
    context_object_name = "todos"

class TodoDetailView(DetailView):
    model = Todo
    template_name = "todo_detail.html"

class TodoCreateView(CreateView):
    model = Todo
    template_name = "todo_form.html"
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("todo-list")

class TodoUpdateView(UpdateView):
    model = Todo
    template_name = "todo_form.html"
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("todo-list")

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todo_confirm_delete.html"
    success_url = reverse_lazy("todo-list")
