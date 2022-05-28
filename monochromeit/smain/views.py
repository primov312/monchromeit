from lib2to3.pytree import convert
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .forms import FilesForm
from .butcher import batchit


def home(request):
    converted = []
    if request.method == 'POST':
        form = FilesForm(request.POST, files = request.FILES)
        if form.is_valid():
            converted = batchit(request.FILES.getlist('files'))
    else:
        form = FilesForm()
    
    cont = {
        'title': 'Home',
        'form': form,
        'converted': converted,
    }
    return render(request = request, template_name = 'smain/index.html', context = cont)