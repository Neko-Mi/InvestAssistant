# Generated by Django 3.0.7 on 2020-06-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200607_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='rec_day',
            field=models.FloatField(default=0),
        ),
    ]
