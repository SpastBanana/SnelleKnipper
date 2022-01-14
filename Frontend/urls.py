from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name="home"),
    path('login', views.loginView, name="home"),
    path('logout', views.logoutView, name="Logout"),
    path('tarieven', views.tarievenView, name="Tarieven"),
    path('overMij', views.overMijView, name="OverMij"),
]