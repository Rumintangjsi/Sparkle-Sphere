from django.shortcuts import render


def show_main(request):
    context = {
        'name': 'Rumintang Jessica H',
        'app' : 'Sparkle Sphere',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)