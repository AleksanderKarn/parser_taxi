from django import views
from django.urls import path

from arenda_avito.views import abc_func

urlpatterns = [
    path('abc_func', views.abc_func, name='abc_func')

]