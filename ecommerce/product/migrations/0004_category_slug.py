# Generated by Django 3.1.2 on 2021-03-06 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_is_import'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
