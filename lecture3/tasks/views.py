from django.shortcuts import render

from lecture3 import tasks

tasks = ['foo', 'bar', 'boo']


def index(request):
    return render(request, 'tasks/index.html', {
        'tasks': tasks
    })
