from django.conf.urls import url
from django.contrib import admin
from login import views
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^base/', views.base),
    url(r'^captcha', include('captcha.urls')),
]

