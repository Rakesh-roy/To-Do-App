from django.contrib import messages
from django.shortcuts import render, redirect
from Todo.models import TodoModel
from Todo.forms import ToDoForm

# Create your views here.
def showIndex(request):
    return render(request,'index.html',{"todo":TodoModel.objects.all().order_by('id')})


def add_todo(request):
    form = ToDoForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request,'You Added One ToDo')
            return redirect('home')
        else:
            messages.error(request, form.errors)
            return redirect('add_todo')
    return render(request,'add_todo.html',{'form':form})


def delete(request):
    todo_id = request.GET.get('id')
    TodoModel.objects.get(id=todo_id).delete()
    messages.success(request, 'You Lost One ToDo')
    return redirect('home')


def update(request):
    todo_id = request.GET.get('id')
    todo = TodoModel.objects.get(id=todo_id)
    if request.method == "POST":
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,'You Updated One ToDo')
            return redirect('home')
    else:
        form = ToDoForm(instance=todo)
        return render(request,'update_todo.html',{'form':form})

