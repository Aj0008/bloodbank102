from django.urls import path

from . import views

urlpatterns = [
    path ('',views.red, name='red'),
    path ('insert',views.insert, name='insert'),
    path ('display', views.display, name='display'),
    path ('login', views.login, name='login'),
    path ('add', views.add, name='add'),
]
