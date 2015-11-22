__author__ = 'narek'

from django.conf.urls import patterns, url
from auto import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))