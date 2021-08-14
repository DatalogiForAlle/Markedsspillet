# Generated by Django 3.2.4 on 2021-06-29 12:11

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0049_auto_20210627_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trader',
            name='prod_cost',
            field=models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
