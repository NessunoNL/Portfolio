from django.db import models

# Create your models here.

class income(models.Model):
    personchoices = [
    ('Jacco', 'Jacco'),
    ('Marjolein', 'Marjolein'),
    ('Joint', 'Gezamenlijk'),
    ]

    categorychoices = [
    ('Maandelijks salaris', 'Maandelijks salaris'),
    ('Wekelijks salaris', 'Wekelijks salaris'),
    ('Eenmalig', 'Eenmalig'),
    ]
    category = models.CharField(max_length=100, choices=categorychoices)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    person = models.CharField(max_length=100, choices=personchoices)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "income"

class incomes(models.Model):
    personchoices = [
    ('Jacco', 'Jacco'),
    ('Marjolein', 'Marjolein'),
    ('Joint', 'Gezamenlijk'),
    ]

    categorychoices = [
    ('Maandelijks', 'Maandelijks'),
    ('Wekelijks', 'Wekelijks'),
    ('Eenmalig', 'Eenmalig'),
    ]
    name = models.CharField(max_length=100, default='undefined')
    category = models.CharField(max_length=100, choices=categorychoices)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    person = models.CharField(max_length=100, choices=personchoices)

    def __str__(self):
        return self.name + ": " + self.person + " - " + self.category

    class Meta:
        verbose_name_plural = "income"

class expenses(models.Model):
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

    category = models.CharField(max_length=100, choices=categorychoices)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    person = models.CharField(max_length=100, choices=personchoices)
    jointbankaccount = models.BooleanField()

    def __str__(self):
        return self.name + " - " + self.person + " - " + str(self.jointbankaccount)

    class Meta:
        verbose_name_plural = "expenses"

class changes(models.Model):
    personchoices = [
    ('Jacco', 'Jacco'),
    ('Marjolein', 'Marjolein'),
    ('Joint', 'Gezamenlijk'),
    ]

    categorychoices = [
    ('income', 'Inkomen'),
    ('expense', 'Uitgave'),
    ]

    category = models.CharField(max_length=100, choices=categorychoices)
    name = name = models.CharField(max_length=100)
    new_amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()
    person = models.CharField(max_length=20, choices=personchoices)

    def __str__(self):
        return self.name + ' --> € ' + str(self.new_amount)

    class Meta:
        verbose_name_plural = "changes"
