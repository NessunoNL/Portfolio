from django.urls import path
from .views import (
ChangeDeleteView,
ChangeCreateView,
IncomeCreateView,
IncomeDeleteView,
ExpenseCreateView,
ExpenseDeleteView
)
from . import views

urlpatterns = [
    path('', views.home, name='budget-home'),
    path('Jacco/', views.Jacco, name='budget-Jacco'),
    path('Marjolein/', views.Marjolein, name='budget-Marjolein'),
    path('changes/', views.changes, name='budget-changes'),
    path('changes/create/', ChangeCreateView.as_view(), name='budget-createchange'),
    path('changes/<int:pk>/delete/', ChangeDeleteView.as_view(), name='budget-deletechange'),
    path('income/create/', IncomeCreateView.as_view(), name='budget-createincome'),
    path('expense/create/', ExpenseCreateView.as_view(), name='budget-createexpense'),
    path('expense/<int:pk>/delete/', ExpenseDeleteView.as_view(), name='budget-deleteexpense'),
    path('income/<int:pk>/delete/', IncomeDeleteView.as_view(), name='budget-deleteincome'),
]
