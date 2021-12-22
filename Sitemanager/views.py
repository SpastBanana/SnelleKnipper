from django.shortcuts import get_object_or_404, redirect, render
from django.core.files.storage import FileSystemStorage
from .models import mainPrice, salePrices, newsBlocks
from .forms import newsForm

def homeView(request):
    data = {
        'page': 'DataLectro-Sitemanager/home.html',
    }
    return render(request, 'DataLectro-Sitemanager/index.html', data)


def priceView(request):

    data = {
        'page': 'DataLectro-Sitemanager/price.html',
    }

    if request.method == 'POST':
        form = mainPrice()
        form.snipPrice = request.POST.get('inputPrice')
        form.save()

    return render(request, 'DataLectro-Sitemanager/index.html', data)


def salesView(request):
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
    saleItem = get_object_or_404(salePrices, pk=saleID)
    deleted = saleItem.saleName
    saleItem.delete()

    data = {
        'page': 'DataLectro-Sitemanager/succesfullDeleted.html',
        'deleted': deleted,
    }

    return render(request, 'DataLectro-Sitemanager/index.html', data)


def newsView(request):
    news = newsBlocks.objects.all()

    data = {
        'page': 'DataLectro-Sitemanager/news.html',
        'news': news,
    }

    if request.method == 'POST' and 'add' in request.POST:
        form = newsForm(request.POST, request.FILES)

        if form.is_valid:
            form.save()

    return render(request, 'DataLectro-Sitemanager/index.html', data)


def delNewsView(request, newsID):
    newsItem = get_object_or_404(newsBlocks, pk=newsID)
    newsItem.img.delete()
    deleted = newsItem.title
    newsItem.delete()

    data = {
        'page': 'DataLectro-Sitemanager/succesfullDeleted.html',
        'deleted': deleted,
    }

    return render(request, 'DataLectro-Sitemanager/index.html', data)













# def addPortPageView(request):

#     data = {
#         'page': 'DataLectro-Sitemanager/addPortPage.html',
#     }

#     if request.method == 'POST':
#         form = addPortPageForm(request.POST, request.FILES)

#         if form.is_valid:
#             form.save()

#         form = portfolioPages()
#         form.portName = request.POST.get('portName')
#         form.img1 = request.POST.get('img1')
#         file1 = request.FILES['img1']
#         form.img2 = request.POST.get('img2')
#         file2 = request.FILES['img2']
#         form.img3 = request.POST.get('img3')
#         file3 = request.FILES['img3']

#         fs = FileSystemStorage()
#         fs.save(file1.name, file1)
#         fs.save(file2.name, file2)
#         fs.save(file3.name, file3)
#         form.save()

#         return render(request, 'DataLectro-Sitemanager/index.html', data)

#     return render(request, 'DataLectro-Sitemanager/index.html', data)


# def deletePortPage(request, portID):
#     portPage = get_object_or_404(portfolioPages, pk=portID)
#     portPage.img1.delete()
#     portPage.img2.delete()
#     portPage.img3.delete()
#     deleted = portPage.portName
#     portPage.delete()

#     data = {
#         'page': 'DataLectro-Sitemanager/succesfullDeleted.html',
#         'deleted': deleted,
#     }

#     return render(request, 'DataLectro-Sitemanager/index.html', data)