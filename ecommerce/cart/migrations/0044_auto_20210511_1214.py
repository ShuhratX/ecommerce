# Generated by Django 3.1.2 on 2021-05-11 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0043_auto_20210508_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderbeta',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
