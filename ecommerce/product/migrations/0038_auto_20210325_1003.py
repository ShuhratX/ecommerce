# Generated by Django 3.1.2 on 2021-03-25 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0037_categoryproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattributes',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
