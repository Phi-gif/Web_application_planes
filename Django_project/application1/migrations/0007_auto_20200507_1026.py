# Generated by Django 2.2.5 on 2020-05-07 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0006_auto_20200507_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airports_arr',
            name='lat',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='airports_arr',
            name='lon',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='airports_dep',
            name='lat',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='airports_dep',
            name='lon',
            field=models.CharField(max_length=30),
        ),
    ]
