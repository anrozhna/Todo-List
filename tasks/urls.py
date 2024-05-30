from django.urls import path

from tasks import views
from tasks.views import IndexView, TaskCreateView

app_name = "tasks"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
]
