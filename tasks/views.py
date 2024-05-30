from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from tasks.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    template_name = "tasks/index.html"
    paginate_by = 3


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")


class ChangeIsCompletedView(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        task_id = self.kwargs.get("pk")
        task = get_object_or_404(Task, pk=task_id)
        task.is_completed = not task.is_completed
        task.save()
        page_number = self.request.POST.get("page", 1)
        return f"{reverse("tasks:index")}?page={page_number}"


class TagListView(generic.ListView):
    model = Tag
    template_name = "tasks/tag_list.html"
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
