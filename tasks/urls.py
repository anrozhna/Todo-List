from django.urls import path

from tasks import views
from tasks.views import IndexView, TaskCreateView, TaskUpdateView

app_name = "tasks"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
]
