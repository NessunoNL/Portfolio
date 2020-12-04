from django.urls import path
from .views import ChangeDeleteView, ChangeCreateView
from . import views

urlpatterns = [
    path('', views.home, name='budget-home'),
    path('Jacco/', views.Jacco, name='budget-Jacco'),
    path('Marjolein/', views.Marjolein, name='budget-Marjolein'),
    path('changes/', ChangeCreateView.as_view(), name='budget-changes'),
    path('changes/<int:pk>/delete/', ChangeDeleteView.as_view(), name='change-delete'),
]
