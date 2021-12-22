from django.urls import path
from Sitemanager import views

urlpatterns = [
    path('', views.homeView, name="sitemanager"),
    path('home', views.homeView, name="sitemanager"),
    path('knipprijs', views.priceView, name="knipprijs"),
    path('kortingen', views.salesView, name="kortingen"),
    path('kortingen/delete/<int:saleID>', views.delSaleView, name="deleteSale"),
    path('nieuws', views.newsView, name="nieuws"),
    path('nieuws/delete/<int:newsID>', views.delNewsView, name="nieuws"),
]
