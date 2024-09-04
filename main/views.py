from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2306240074',
        'name': 'Aditya Dharma',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
