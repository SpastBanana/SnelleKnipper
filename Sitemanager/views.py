from django.shortcuts import get_object_or_404, redirect, render
from django.core.files.storage import FileSystemStorage
from .models import mainPrice, salePrices
from Sitemanager.models import mainPrice, openedTimes

def homeView(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    data = {
        'page': 'DataLectro-Sitemanager/home.html',
    }
    return render(request, 'DataLectro-Sitemanager/index.html', data)


def priceView(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    data = {
        'page': 'DataLectro-Sitemanager/price.html',
        'knipprijs': mainPrice.objects.last(),
    }

    if request.method == 'POST':
        form = mainPrice()
        form.snipPrice = request.POST.get('inputPrice')
        form.save()

        return redirect('/sitemanager/knipprijs')

    return render(request, 'DataLectro-Sitemanager/index.html', data)


def salesView(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    kortingen = salePrices.objects.all()

    data = {
        'page': 'DataLectro-Sitemanager/sales.html',
        'kortingen': kortingen,
    }

    if request.method == 'POST' and 'add' in request.POST:
        form = salePrices()
        form.saleName = request.POST.get('saleName')
        form.salePrice = request.POST.get('salePrice')
        form.save()

    return render(request, 'DataLectro-Sitemanager/index.html', data)


def delSaleView(request, saleID):
    if not request.user.is_authenticated:
        return redirect('/login')

    saleItem = get_object_or_404(salePrices, pk=saleID)
    deleted = saleItem.saleName
    saleItem.delete()

    data = {
        'page': 'DataLectro-Sitemanager/succesfullDeleted.html',
        'deleted': deleted,
    }

    return render(request, 'DataLectro-Sitemanager/index.html', data)


def openTimes(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    times = openedTimes.objects.all()

    if request.method == 'POST' and 'change' in request.POST:
        day = request.POST.get('day')
        form = openedTimes.objects.get(openedDay=f'{day}')
        form.openedTime = request.POST.get('time')
        form.save()

    data = {
        'page': 'DataLectro-Sitemanager/opened.html',
        'opened': openedTimes.objects.all(),
    }

    return render(request, 'DataLectro-Sitemanager/index.html', data)