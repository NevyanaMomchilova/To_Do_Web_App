from django.shortcuts import render, redirect
from .models import Task
from .forms import FormTask


def index(request):
    all_tasks = Task.objects.all()
    context = {"all_tasks": all_tasks}
    return render(request, "tasks/index.html", context)


def tasks_manager(request):
    form = FormTask
    all_tasks = Task.objects.all()
    context = {
        "form": form,
        "all_tasks": all_tasks,
    }

    if request.method == "POST":
        form = FormTask(request.POST)
        if form.is_valid():
            form.save()

            # to clear the form after submitting a task:
            form = FormTask()

            # return redirect("tasks:tasks_manager")
    return render(request, "tasks/task_manager.html", context)


def delete_task(request, pk):
    item = Task.objects.get(id=pk)
    item.delete()

    return redirect("tasks:tasks_manager")


