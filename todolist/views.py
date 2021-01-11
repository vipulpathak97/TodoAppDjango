from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist.models import Task
from todolist.forms import Taskform
from django.contrib import messages

# Create your views here.
def todolist(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success': True}
    return render(request, 'index.html', context)

def tasks(request):
    allTasks = Task.objects.all()
    
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)

def delete(request, list_id):
    item = Task.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted!'))
    return redirect('tasks')

def update_task(request, list_id):
    if request.method == "POST":
        item = Task.objects.get(pk=list_id)

        form = Taskform(request.POST or None, instance=item)

        if form.is_valid():
            messages.success(request, ('Item has been Updated!'))
            form.save()
            return redirect("index")
    else:
        item = Task.objects.get(pk=list_id)
        return render(request, "update_task.html", {"item": item})

