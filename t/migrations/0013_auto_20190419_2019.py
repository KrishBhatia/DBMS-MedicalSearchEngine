# Generated by Django 2.1 on 2019-04-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t', '0012_auto_20190419_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='drug',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='type',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='store',
            name='city',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]