# Generated by Django 3.1.2 on 2021-03-16 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20210315_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariation',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='product.product'),
        ),
    ]
