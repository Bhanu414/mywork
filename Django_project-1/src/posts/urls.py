from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name = 'post_detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name = 'post_update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    url(r'^$', post_list,name='list'),

]
