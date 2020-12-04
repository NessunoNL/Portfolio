from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='budget-home'),
    path('Jacco/', views.Jacco, name='budget-Jacco'),
    path('Marjolein/', views.Marjolein, name='budget-Marjolein'),
    path('changes/', views.changes, name='budget-changes'),
]
