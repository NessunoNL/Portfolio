from django.contrib import admin
from .models import incomes, expenses, changes
# Register your models here.
admin.site.register(incomes)
admin.site.register(expenses)
admin.site.register(changes)
