from django.urls import path

from Test import stylegan

urlpatterns = [

    path('setvalue', stylegan.dispatcher),
    path('path',stylegan.geturl)
]