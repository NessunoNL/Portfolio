# Generated by Django 3.1.3 on 2020-12-04 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_auto_20201204_1403'),
    ]

    operations = [
        migrations.DeleteModel(
            name='income',
        ),
        migrations.AddField(
            model_name='changes',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
