# Generated by Django 3.1.11 on 2021-06-05 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0028_auto_20210605_0545'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='num_sold_unit',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]