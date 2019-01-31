# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

autor = models.ForeignKey(User, on_delete=models.CASCADE)

class Lekarz(models.Model):
    nazwa = models.CharField(verbose_name='Lekarz', max_length=30)
    opis = models.TextField(blank=True, help_text='Opis Lekarza')
    cena = models.DecimalField(max_digits=5, decimal_places=0)
    data = models.DateField('dodano', auto_now_add=True)


    def __unicode__(self):
        return u'%s' % (self.nazwa)


class Specjalizacja(models.Model):
    lekarz = models.ForeignKey(Lekarz,
                              on_delete=models.CASCADE,
                              related_name='specjalizacje')
    nazwa = models.CharField(verbose_name=u"specjalizacja", max_length=30)
    dzieci = models.BooleanField(
        default=False,
        verbose_name=u"Czy dla osob ponizej 18 lat?",
        help_text=u"Zaznacz, jeżeli składnik jest odpowiedni dla"
                  u" dzieci")

    def __unicode__(self):
        return u'%s' % (self.nazwa)



class Godziny(models.Model):
    lekarz = models.ForeignKey(Lekarz,
                              on_delete=models.CASCADE,
                              related_name='godziny')
    nazwa = models.CharField(verbose_name=u"godziny", max_length=30)
    godzina = models.DateField(

        verbose_name=u"Dodaj godzine",
        help_text=u"Zaznacz, jeżeli składnik jest odpowiedni dla"
                  u" dzieci")

    def __unicode__(self):
        return u'%s' % (self.nazwa)


class Meta:
        verbose_name_plural = 'lekarze'