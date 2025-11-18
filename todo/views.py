from django.shortcuts import render, redirect
from .models import Task
from django.db.models import Case, When, Value, IntegerField 

def index(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        priority = request.POST.get('priority')
        if title:
            Task.objects.create(title=title, priority=priority)
        return redirect('index')

    search_query = request.GET.get('q')
    
    if search_query:
        tasks = Task.objects.filter(title__icontains=search_query)
    else:
        tasks = Task.objects.all()

    
    tasks = tasks.annotate(
        custom_order=Case(
            When(priority='High', then=Value(1)),
            When(priority='Medium', then=Value(2)),
            When(priority='Low', then=Value(3)),
            default=Value(4),
            output_field=IntegerField(),
        )
    ).order_by('custom_order', '-created_at') 

    return render(request, 'index.html', {'tasks': tasks})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')

def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('index')