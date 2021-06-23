# Generated by Django 3.2.4 on 2021-06-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0038_alter_trader_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='product_name_plural',
            field=models.CharField(default='a', max_length=16),
        ),
        migrations.AddField(
            model_name='market',
            name='product_name_singular',
            field=models.CharField(default='a', max_length=16),
        ),
        migrations.AlterField(
            model_name='market',
            name='product_name',
            field=models.CharField(default='a', max_length=16),
        ),
    ]