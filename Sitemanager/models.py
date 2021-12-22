from typing import DefaultDict
from django.db import models


class mainPrice(models.Model):
    snipPrice = models.CharField(max_length=30)

    def __str__(self):
        return self.snipPrice

    class Meta:
        verbose_name_plural = "Hoofdprijs gewone knipbeurt"


class salePrices(models.Model):
    saleName = models.CharField(max_length=30)
    salePrice = models.CharField(max_length=30)

    def __str__(self):
        return self.saleName

    class Meta:
        verbose_name_plural = "Korting namen en prijzen"


class newsBlocks(models.Model):
    styleChoises = {
        ('Rood', 'Rood'),
        ('Groen', 'Groen'),
        ('Blauw', 'Blauw'),
        ('Geen', 'Geen'),
    }
    title = models.CharField(max_length=30)
    img = models.ImageField(upload_to="newsImages", default='none.png')
    borderSelect = models.CharField(max_length=255, choices=styleChoises)
    alinea1 = models.TextField(max_length=150)
    alinea2 = models.TextField(max_length=150)
    alinea3 = models.TextField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Niews blokken"