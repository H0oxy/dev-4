from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import random
from mainapp.models import Numbers
@login_required


def index(request):
    numbers = Numbers.objects.all()
    context = {
        'page_title': 'Рандомайзер',
        'numbers': random.choices(numbers),
    }
    return render(request, 'mainapp/index.html', context)

def index(request):
    numbers = Numbers.objects.all()
    context = {
        'page_title': 'Рандомайзер',
        'numbers': random.choices(numbers),
    }
    return render(request, 'mainapp/index.html', context)
