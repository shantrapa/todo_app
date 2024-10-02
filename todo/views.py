from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/index.html', context)

def toggle_complete(request, pk):
    task = Task.objects.get(id=pk)
    task.isComplete = not task.isComplete
    task.save()
    return JsonResponse({'status': 'success', 'isComplete': task.isComplete})

def rename(request, pk):
    task = Task.objects.get(id=pk)
    new_name = request.POST.get('new_name', '')
    if new_name:
        task.name = new_name
        task.save()
        return JsonResponse({'status': 'success', 'new_name': task.name})
    return JsonResponse({'status': 'failure'})

def delete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failure'})