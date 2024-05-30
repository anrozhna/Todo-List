from django.urls import path

from tasks.views import (
    IndexView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    ChangeIsCompletedView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)

app_name = "tasks"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tasks/<int:pk>/completed/",
        ChangeIsCompletedView.as_view(),
        name="task-completed"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
]
