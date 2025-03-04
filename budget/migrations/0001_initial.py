# Generated by Django 3.1.3 on 2020-11-29 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='changes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('income', 'Inkomen'), ('expense', 'Uitgave')], max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('new_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('month', models.DateField()),
                ('person', models.CharField(choices=[('Jacco', 'Jacco'), ('Marjolein', 'Marjolein'), ('Joint', 'Gezamenlijk')], max_length=20)),
            ],
            options={
                'verbose_name_plural': 'changes',
            },
        ),
        migrations.CreateModel(
            name='expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Energie', 'Energie en voorzieningen'), ('Telecom', 'Telecom'), ('Onderdak', 'Onderdak'), ('Transport', 'Transport'), ('Levensmiddelen', 'Levensmiddelen'), ('Verzekering', 'Verzekering'), ('Schuld', 'Schuld'), ('Entertainment', 'Entertainment')], max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('person', models.CharField(choices=[('Jacco', 'Jacco'), ('Marjolein', 'Marjolein'), ('Joint', 'Gezamenlijk')], max_length=100)),
                ('jointbankaccount', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'expenses',
            },
        ),
        migrations.CreateModel(
            name='income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Maandelijks salaris', 'Maandelijks salaris'), ('Wekelijks salaris', 'Wekelijks salaris'), ('Eenmalig', 'Eenmalig')], max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('person', models.CharField(choices=[('Jacco', 'Jacco'), ('Marjolein', 'Marjolein'), ('Joint', 'Gezamenlijk')], max_length=100)),
            ],
            options={
                'verbose_name_plural': 'income',
            },
        ),
        migrations.CreateModel(
            name='incomes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='undefined', max_length=100)),
                ('category', models.CharField(choices=[('Maandelijks salaris', 'Maandelijks salaris'), ('Wekelijks salaris', 'Wekelijks salaris'), ('Eenmalig', 'Eenmalig')], max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('person', models.CharField(choices=[('Jacco', 'Jacco'), ('Marjolein', 'Marjolein'), ('Joint', 'Gezamenlijk')], max_length=100)),
            ],
            options={
                'verbose_name_plural': 'income',
            },
        ),
    ]
