# Generated by Django 3.2.4 on 2021-08-23 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0058_auto_20210818_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='max_rounds',
            field=models.IntegerField(blank=True, default=15, null=True),
        ),
    ]
