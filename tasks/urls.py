from django.urls import path

from tasks import views
from tasks.views import IndexView

app_name = "tasks"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
