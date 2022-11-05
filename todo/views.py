from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.
def index(req):

    todo = Todo.objects.all()

    if req.method == 'POST':
        new_todo = Todo(
            title = req.POST['title']
        )
        new_todo.save()
        return redirect('/')
    return render(req, 'index.html', {'todos': todo})

def delete(req, pk):
    todo = Todo.objects.get(id = pk)
    todo.delete()
    return redirect('/')