# Generated by Django 3.1.2 on 2021-03-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0036_delete_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.PositiveIntegerField()),
                ('product_id', models.PositiveIntegerField()),
            ],
        ),
    ]