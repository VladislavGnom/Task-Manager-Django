from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import CreateTaskForm, EditTaskForm


def show_tasks(request):
    tasks = Task.objects.all()

    context = {'title': '',
               'tasks': tasks,
               }
    
    return render(request, 'app/show_tasks.html', context=context)

def create_task(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)

        if form.is_valid():
            new_task = form.save(commit=False)
            
            # other logics

            new_task.save()

            return redirect('show_tasks')
    else:
        form = CreateTaskForm()

    context = {'title': 'Create Task',
               'form': form,
               }

    return render(request, 'app/create_task.html', context=context)


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    task.delete()

    return redirect('show_tasks')

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = EditTaskForm(request.POST, instance=task)

        if form.is_valid():
            new_task = form.save(commit=False)

            # other logics 

            new_task.save()

            return redirect('show_tasks')
    else:
        form = EditTaskForm(instance=task)

    context = {'title': 'Edit Task',
               'form': form,
               }

    return render(request, 'app/edit_task.html', context=context)


def change_list(request, task_id, is_complete):
    task = get_object_or_404(Task, pk=task_id)
    if is_complete == 'complete':
        task.is_complete = True
        task.save()
    elif is_complete == 'uncomplete':
        task.is_complete = False
        task.save()
        

    return redirect('show_tasks')

