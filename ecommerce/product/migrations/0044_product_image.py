# Generated by Django 3.1.5 on 2021-03-26 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0043_auto_20210326_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
