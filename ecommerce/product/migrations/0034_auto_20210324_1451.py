# Generated by Django 3.1.2 on 2021-03-24 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0033_auto_20210324_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattributes',
            name='is_main',
            field=models.BooleanField(default=True),
        ),
    ]