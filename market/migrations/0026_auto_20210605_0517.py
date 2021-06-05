# Generated by Django 3.1.11 on 2021-06-05 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0025_merge_20210604_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='max_cost',
            field=models.PositiveIntegerField(default=8),
        ),
        migrations.AlterField(
            model_name='market',
            name='min_cost',
            field=models.PositiveIntegerField(default=8),
        ),
    ]