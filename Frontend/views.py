from django.shortcuts import render
from Sitemanager.models import mainPrice, salePrices, newsBlocks

def homeView(request):
    knippie = mainPrice.objects.last()
    kortie = salePrices.objects.all()
    news = newsBlocks.objects.all()

    data = {
        'page': 'home.html',
        'mainPrice': knippie,
        'kortingen': kortie,
        'news': news,
    }

    return render(request, 'index.html', data)