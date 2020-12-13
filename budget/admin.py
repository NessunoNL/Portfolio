from django.contrib import admin
from .models import Incomes, Expenses, Changes
# Register your models here.
admin.site.register(Incomes)
admin.site.register(Expenses)
admin.site.register(Changes)
