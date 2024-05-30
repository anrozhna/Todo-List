from django.shortcuts import render
from django.views import generic

from tasks.models import Task


class IndexView(generic.ListView):
    model = Task
    template_name = "tasks/index.html"
    paginate_by = 3
