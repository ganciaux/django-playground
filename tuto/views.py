from django.shortcuts import get_object_or_404, render

def index(request):
    return render(request, 'tuto/index.html', {})

def index2(request):
    return render(request, 'tuto2/index.html', {})
