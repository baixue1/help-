from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^index/$', views.blog_index),
    url(r'^admin/', admin.site.urls)
]
