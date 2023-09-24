from django.urls import path
from . import views

urlpatterns = [
    path('getItem', views.getItem),
    path('addItem', views.addItem),
    path('sqlquery', views.getSqlQuery),
    path('addCustomer', views.addCustomer),
    path('getScores', views.getScores)
]