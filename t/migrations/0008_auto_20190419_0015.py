# Generated by Django 2.1 on 2019-04-18 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t', '0007_auto_20190418_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='store',
            name='pincode',
            field=models.PositiveIntegerField(),
        ),
    ]
