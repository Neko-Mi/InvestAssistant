# Generated by Django 3.0.7 on 2020-06-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200605_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='price_predict_3',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='price_predict_6',
            field=models.FloatField(default=0),
        ),
    ]
