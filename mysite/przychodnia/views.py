# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import models
from . import forms
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import DetailView


def index(request):
    """Strona główna"""
    kontekst = {'komunikat': 'Witaj w aplikacji przychodnia!'}
    return render(request, 'przychodnia/index.html', kontekst)

@method_decorator(login_required, 'dispatch')
class LekarzCreate(CreateView):
    """Widok dodawania lekarzy i specjalizacji."""

    model = models.Lekarz
    form_class = forms.LekarzForm
    success_url = reverse_lazy('przychodnia:lista')  # '/przychodnia/lista'

    def get_context_data(self, **kwargs):
        context = super(LekarzCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['specjalizacja'] = forms.SpecjalizacjaFormSet(self.request.POST)
        else:
            context['specjalizacja'] = forms.SpecjalizacjaFormSet()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        specjalizacja = forms.SpecjalizacjaFormSet(self.request.POST)
        if form.is_valid() and specjalizacja.is_valid():
            return self.form_valid(form, specjalizacja)
        else:
            return self.form_invalid(form, specjalizacja)

    def form_valid(self, form, specjalizacja):
        form.instance.autor = self.request.user
        self.object = form.save()
        specjalizacja.instance = self.object
        specjalizacja.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, specjalizacja):
        return self.render_to_response(
            self.get_context_data(form=form, specjalizacja=specjalizacja)
        )

@method_decorator(login_required, 'dispatch')
class LekarzDelete(DeleteView):
    model = models.Lekarz
    success_url = reverse_lazy('przychodnia:lista')  # '/pizza/lista'

    def get_context_data(self, **kwargs):
        context = super(LekarzDelete, self).get_context_data(**kwargs)
        specjalizacja = models.Godziny.objects.filter(lekarz=self.object)
        context['specjalizacje'] = specjalizacja

        return context


@method_decorator(login_required, 'dispatch')
class LekarzDetailGodziny(DetailView):
    model = models.Lekarz
    success_url = reverse_lazy('przychodnia:lista')
    def get_context_data(self, **kwargs):
        context = super(LekarzDetailGodziny, self).get_context_data(**kwargs)
        godziny = models.Godziny.objects.filter(lekarz=self.object)
        context['godziny'] = godziny
        return context


@method_decorator(login_required, 'dispatch')
class LekarzDetailView(DetailView):
    model = models.Lekarz
    success_url = reverse_lazy('przychodnia:lista')
    def get_context_data(self, **kwargs):

        context = super(LekarzDetailView, self).get_context_data(**kwargs)
        specjalizacje = models.Specjalizacja.objects.filter(lekarz=self.object)
        context['specjalizacje'] = specjalizacje
        return context