# Generated by Django 3.1.11 on 2021-06-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0032_auto_20210607_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='units_sold',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
