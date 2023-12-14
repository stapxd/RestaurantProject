from django.shortcuts import render


# Create your views here.
def index(request):

    title = 'Головна сторінка'
    return render(request, 'main/index.html', locals())


def about(request):

    title = 'Про нас'
    return render(request, 'main/about.html', locals())
