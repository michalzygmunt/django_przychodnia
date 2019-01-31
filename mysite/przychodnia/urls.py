# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views  # import widoków aplikacji
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import Lekarz

app_name = 'przychodnia'  # przestrzeń nazw aplikacji
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lista/', login_required(ListView.as_view(model=Lekarz)),
        name='lista'),
    url(r'^dodaj/$', views.LekarzCreate.as_view(), name='dodaj'),
    url(r'^usun/(?P<pk>\d+)/', views.LekarzDelete.as_view(), name='usun'),

    url(r'^godzinki/(?P<pk>\d+)/', views.LekarzDetailGodziny.as_view(), name='godzinki'),

    url(r'^info/(?P<pk>\d+)/', views.LekarzDetailView.as_view(), name='info'),

]