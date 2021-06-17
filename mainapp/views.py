from django.contrib.auth.decorators import login_required
from django.shortcuts import render




def index(request):
    context = {
        'page_title': 'ЛДМШ',
    }
    return render(request, 'mainapp/index.html', context)
