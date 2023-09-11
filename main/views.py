from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Rumintang Jessica H',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)

# Create your views here.
