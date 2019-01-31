# -*- coding: utf-8 -*-
from django.contrib import admin
from . import models
from django.forms import Textarea
from django.db.models.fields import TextField


class SpecjalizacjaInline(admin.TabularInline):
    model = models.Specjalizacja
    fields = ['nazwa', 'dzieci']
    extra = 3
    max_num = 6


class SpecjalizacjaInlinee(admin.TabularInline):
    model = models.Godziny
    fields = ['nazwa', 'godzina']
    extra = 3
    max_num = 6


@admin.register(models.Lekarz)
class LekarzAdmin(admin.ModelAdmin):
    exclude = ('autor',)
    inlines = [SpecjalizacjaInlinee,SpecjalizacjaInline]

    search_fields = ['nazwa']
    list_per_page = 10
    formfield_overrides = {
        TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100})},
    }

    def save_model(self, request, obj, form, change):
        if not change:
            obj.autor = request.user
        obj.save()