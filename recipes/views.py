from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):

    ### Vai buscar o home.html dentro da pasta templates/recipes ou
    ### na pasta base_templates/global/home.html
    ###
    ##return render(request, 'global/home.html')
    return render(request, 'recipes/home.html', context={
        'name': 'Wilson Nunes'
    })

def contato(request):
    return HttpResponse('Contato na View')


def sobre(request):
    return HttpResponse('Sobre na views.py')

