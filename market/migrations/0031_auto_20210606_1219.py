# Generated by Django 3.1.11 on 2021-06-06 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0030_auto_20210605_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trader',
            name='prod_cost',
            field=models.IntegerField(default=1),
        ),
    ]
