# Generated by Django 3.2 on 2022-07-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warranty', '0002_warrantyregistration_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warrantyregistration',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
