# Generated by Django 3.2.8 on 2021-11-03 08:49

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0010_rename_total_prod_cost_change_market_accum_cost_change'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='alpha',
            field=models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]),
        ),
    ]