from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from Sitemanager.models import mainPrice, salePrices, openedTimes

def homeView(request):
    knippie = mainPrice.objects.last()
    kortie = salePrices.objects.all()
    opened = openedTimes.objects.all()

    data = {
        'page': 'home.html',
        'mainPrice': knippie,
        'kortingen': kortie,
        'opened': opened,
    }

    return render(request, 'index.html', data)


def loginView(request):
    if request.method == 'POST' and 'login' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/sitemanager')
            else:
                data = {
                    'page': 'login.html',
                    'error': 'User account not activated',
                }
                return render(request, 'index.html', data)
        else:
            data = {
                'page': 'login.html',
                'error': 'Incorrect password and/or username',
            }
            return render(request, 'index.html', data)

    data = {
        'page': 'login.html',
        'error': '',
    }

    return render(request, 'index.html', data)


def logoutView(request):
    logout(request)
    return redirect('/')