# Generated by Django 3.1.2 on 2021-03-20 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0030_auto_20210320_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderbeta',
            name='status',
            field=models.CharField(choices=[('W', 'Kutilmoqda'), ('S', "Jo'natilgan"), ('F', 'Tugallangan')], max_length=255, null=True),
        ),
    ]
