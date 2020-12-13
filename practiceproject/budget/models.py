from django.db import models

# Create your models here.

# class Income(models.Model):
#     personchoices = [
#     ('Jacco', 'Jacco'),
#     ('Marjolein', 'Marjolein'),
#     ('Joint', 'Gezamenlijk'),
#     ]
#
#     categorychoices = [
#     ('Maandelijks salaris', 'Maandelijks salaris'),
#     ('Wekelijks salaris', 'Wekelijks salaris'),
#     ('Eenmalig', 'Eenmalig'),
#     ]
#     category = models.CharField(max_length=100, choices=categorychoices)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     person = models.CharField(max_length=100, choices=personchoices)
#
#     def __str__(self):
#         return self.category
#
#     class Meta:
#         verbose_name_plural = "income"

class Incomes(models.Model):
    personchoices = [
    ('Jacco', 'Jacco'),
    ('Marjolein', 'Marjolein'),
    ]

    # categorychoices = [
    # ('Maandelijks', 'Maandelijks'),
    # ('Wekelijks', 'Wekelijks'),
    # ]
    name = models.CharField(max_length=100, verbose_name='Naam')
    category = models.CharField(max_length=100, verbose_name='Categorie', default='Maandelijks')
    amount = models.DecimalField(max_digits=10, verbose_name='Bedrag in €', decimal_places=2)
    person = models.CharField(max_length=100, verbose_name='Voor ', choices=personchoices)

    def __str__(self):
        return self.name + ": " + self.person + " - " + self.category

    class Meta:
        verbose_name_plural = "income"

class Expenses(models.Model):
    personchoices = [
    ('Jacco', 'Jacco'),
    ('Marjolein', 'Marjolein'),
    ('Joint', 'Gezamenlijk'),
    ]

    categorychoices = [
    ('Energie', 'Energie en voorzieningen'),
    ('Telecom', 'Telecom'),
    ('Onderdak', 'Onderdak'),
    ('Transport', 'Transport'),
    ('Levensmiddelen', 'Levensmiddelen'),
    ('Verzekering', 'Verzekering'),
    ('Schuld', 'Schuld'),
    ('Entertainment', 'Entertainment'),
    ('Gezondheid', 'Gezondheid'),
    ]

    category = models.CharField(max_length=100, verbose_name='Categorie', choices=categorychoices)
    name = models.CharField(max_length=100, verbose_name='Naam')
    amount = models.DecimalField(max_digits=10, verbose_name='Bedrag in €_', decimal_places=2)
    person = models.CharField(max_length=100, verbose_name='Voor ', choices=personchoices)
    jointbankaccount = models.BooleanField(verbose_name='Betalen naar gezamenlijke? ')

    def __str__(self):
        if self.person == 'Joint':
            _person = 'allebei'
        else:
            _person = self.person
        return f'{self.name} - {_person}: € {self.amount}'

    class Meta:
        verbose_name_plural = "expenses"

class Changes(models.Model):
    personchoices = [
    ('Jacco', 'Jacco'),
    ('Marjolein', 'Marjolein'),
    ('Joint', 'Gezamenlijk'),
    ]

    categorychoices = [
    ('income', 'Inkomen'),
    ('expense', 'Uitgave'),
    ]

    name = models.ForeignKey(Expenses, verbose_name='Uitgave', on_delete=models.CASCADE)
    new_amount = models.DecimalField(max_digits=10, verbose_name='Nieuw bedrag in €', decimal_places=2)
    date = models.DateField(verbose_name='Datum')
    completed = models.BooleanField(default=False, verbose_name='Reeds voltooid?')

    def __str__(self):
        if self.name.person == 'Joint':
            _person = 'allebei'
        else:
            _person = self.name.person
        return f' {self.date.day}-{self.date.month}-{self.date.year}: {self.name.name} naar € {self.new_amount} voor {_person}'

    class Meta:
        verbose_name_plural = "changes"
