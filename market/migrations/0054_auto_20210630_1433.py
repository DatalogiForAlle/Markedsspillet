# Generated by Django 3.2.4 on 2021-06-30 12:33

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0053_auto_20210630_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='max_cost',
            field=models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='market',
            name='min_cost',
            field=models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
