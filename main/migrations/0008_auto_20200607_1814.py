# Generated by Django 3.0.7 on 2020-06-07 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_stock_rec_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='reg_day_future',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='stock',
            name='reg_day_past',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='rec_day',
            field=models.DateField(default='2000-01-01'),
        ),
    ]
