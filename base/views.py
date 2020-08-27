from django.shortcuts import render
from .models import BaseUser, Categoria, Movimento


def index(request):
    user = BaseUser.objects.filter(email='nathanbabahia@gmail.com')[0]
    receitas = Movimento.objects.filter(user=user.id)

    context = {
        'receitas': receitas,
        }
    return render(request, 'index.html', context)
