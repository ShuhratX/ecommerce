# Generated by Django 3.1.5 on 2021-03-21 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_slider_is_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariation',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
