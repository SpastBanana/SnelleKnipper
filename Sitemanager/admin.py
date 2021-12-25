from django.contrib import admin
from .models import mainPrice, salePrices, openedTimes

admin.site.register(mainPrice)
admin.site.register(salePrices)
admin.site.register(openedTimes)