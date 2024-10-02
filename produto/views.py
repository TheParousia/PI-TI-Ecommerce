from django.shortcuts import render

def pagina_home(request):
    return render(request, 'pagina_home.html')
