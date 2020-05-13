from django.urls import path
from tasks import views


app_name = "tasks"

urlpatterns = [
    path("", views.tasks_manager, name="tasks_manager"),
    path("delete/<int:pk>/", views.delete_task, name="delete")
]

