# Generated by Django 2.2.5 on 2020-05-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0005_auto_20200507_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airports_arr',
            name='airport_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='airports_dep',
            name='airport_name',
            field=models.CharField(max_length=100),
        ),
    ]