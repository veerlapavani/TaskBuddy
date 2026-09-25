from django.shortcuts import render, redirect
from .models import Task


def dashboard(request):
    tasks = Task.objects.all().order_by('-created_at')
    completed_tasks = Task.objects.filter(completed=True).count()
    total_tasks = Task.objects.count()

    return render(request, 'tasks/dashboard.html', {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'total_tasks': total_tasks,
    })

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        category = request.POST.get('category')

        Task.objects.create(
            title=title,
            description=description,
            priority=priority,
            category=category
        )

        return redirect('dashboard')

    return render(request, 'tasks/create_task.html')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('dashboard')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('dashboard')


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.priority = request.POST.get('priority')
        task.category = request.POST.get('category')
        task.save()

        return redirect('dashboard')

    return render(request, 'tasks/edit_task.html', {'task': task})