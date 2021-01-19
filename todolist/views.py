import django
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.urls import reverse
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def todolist(request):
    
    #context = {'success': False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']        
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        print(ins, "this is the added")
        item = Task.objects.get(taskTitle=title)
        print(item.id, "this is the id")
        logger.error("logger")
        #context = {'success': True}
        messages.success(request, ('Item has been Added'))
        return redirect('tasks')
    return render(request, 'index.html')

def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)

def delete(request, list_id):
    item = Task.objects.get(pk=list_id)
    item.delete()
    print("deleted")
    print(item.id, "deleted id")
    messages.success(request, ('Item has been deleted'))
    return redirect('tasks')

def update_task(request, list_id):
    if request.method == "POST":
        item = Task.objects.get(pk=list_id)
        print(item, "this is the item")
        print(item.taskDesc)
        print(item.taskTitle, "this is the title")
        title = request.POST['title']
        desc = request.POST['desc']
        item.taskTitle=title
        item.taskDesc=desc
        item.save()
        print(item, "updated")
        print(Task.objects.get(id=list_id))
        print(title, desc, "this is the updated")
              
        #ins = Task(taskTitle=title, taskDesc=desc)
        #ins.save()
        allTasks = Task.objects.all()
        context = {'tasks': allTasks}
        #id1 = list_id
        #return render(request, 'tasks.html', context)
        return redirect('tasks')

    
    
    
    
    
    
    #if request.method == "POST":
        #item = Task.objects.get(id=list_id)
        #form = TaskForm(request.POST, instance=item)

        #if form.is_valid():
            #form.save()
            #messages.success(request, ('Item has been Updated!'))
            #return redirect("tasks")
    #else:
        #item = Task.objects.get(id=list_id)
        #return render(request, 'tasks.html', {'form': form})

