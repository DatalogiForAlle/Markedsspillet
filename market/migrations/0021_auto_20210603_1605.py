# Generated by Django 3.1.11 on 2021-06-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0020_auto_20210603_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='profit',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]