from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from .forms import Todoforms
from . models import Task

# class TaskListView(ListView):
#     model = Task
#     Template_name = '<Task>/task_view.html'
#     context_object_name = 'obj1'

def task_view(request):
    obj1=Task.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        obj=Task(name=name,priority=priority,date=date)
        obj.save()
    return render(request,"task_view.html",{'obj1':obj1})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':task})

def update(request,id):
    task=Task.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'form':form})