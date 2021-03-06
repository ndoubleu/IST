# Generated by Django 3.2 on 2022-03-02 06:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firm', '0004_auto_20220302_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firmmodel',
            name='phone_number',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator(message='Неверный формат номера телефона', regex='^998\\d{9}$')], verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='firmmodel',
            name='website',
            field=models.URLField(verbose_name='Веб сайт'),
        ),
    ]
