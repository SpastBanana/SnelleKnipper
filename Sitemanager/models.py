from typing import DefaultDict
from django.db import models


class openedTimes(models.Model):
    openedDay = models.CharField(max_length=30)
    openedTime = models.CharField(max_length=30)

    def __str__(self):
        return self.openedDay

    class Meta:
        verbose_name_plural = "Openings tijden"


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