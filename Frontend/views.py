from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from Sitemanager.models import mainPrice, salePrices, openedTimes

def homeView(request):
    opened = openedTimes.objects.all()

    data = {
        'page': 'home.html',
        'opened': opened,
    }

    return render(request, 'index.html', data)


def tarievenView(request):

    data = {
        'page': 'tarieven.html',
        'opened': openedTimes.objects.all(),
        'sales': salePrices.objects.all(),
        'price': mainPrice.objects.last(),
    }

    return render(request, 'index.html', data)


def overMijView(request):
    opened = openedTimes.objects.all()

    data = {
        'page': 'overMij.html',
        'opened': opened,
    }

    return render(request, 'index.html', data)


def loginView(request):
    opened = openedTimes.objects.all()

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
                    'opened': opened,
                }
                return render(request, 'index.html', data)
        else:
            data = {
                'page': 'login.html',
                'error': 'Incorrect password and/or username',
                'opened': opened,
            }
            return render(request, 'index.html', data)

    data = {
        'page': 'login.html',
        'error': '',
        'opened': opened,
    }

    return render(request, 'index.html', data)


def logoutView(request):
    logout(request)
    return redirect('/')