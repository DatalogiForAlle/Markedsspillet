# Generated by Django 3.1.7 on 2021-04-01 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20210329_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='trader',
            name='ready',
            field=models.BooleanField(default=False),
        ),
    ]
