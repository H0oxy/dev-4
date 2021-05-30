from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import random
from mainapp.models import Numbers
@login_required


# def index(request):
#     numbers = Numbers.objects.all()
#     context = {
#         'page_title': 'Рандомайзер',
#         'numbers': random.choices(numbers),
#     }
#     return render(request, 'mainapp/index.html', context)

def index(request):
    _num = random.randint(1,12)
    num = str(_num)
    context = {
        'page_title': 'Рандомайзер',
        'num': num.replace(' ', ''),    # replace isn't working
    }
    return render(request, 'mainapp/index.html', context)
