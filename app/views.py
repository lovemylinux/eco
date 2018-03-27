from django.shortcuts import render

# Create your views here.


def show_index(request):
    return render(request, 'index.html')


def show_travel(request):
    return render(request, 'travel.html')


def show_happiness(request):
    return render(request, 'happiness.html')