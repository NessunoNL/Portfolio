# Generated by Django 3.1.3 on 2020-12-04 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_auto_20201204_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changes',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.expenses'),
        ),
    ]
