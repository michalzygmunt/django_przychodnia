# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea
from . import models
from django.forms.models import inlineformset_factory


class LekarzForm(ModelForm):

    class Meta:
        model = models.Lekarz
        exclude = ('data', 'autor')
        widgets = {'opis': Textarea(attrs={'rows': 2, 'cols': 80})}


SpecjalizacjaFormSet = inlineformset_factory(
    parent_model=models.Lekarz,
    model=models.Specjalizacja,
    max_num=6,
    min_num=1,
    validate_max=True,
    validate_min=True,
    extra=2,
    fields=('nazwa', 'dzieci')
)

