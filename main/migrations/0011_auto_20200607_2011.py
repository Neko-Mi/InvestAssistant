# Generated by Django 3.0.7 on 2020-06-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_stock_reg_day_past'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='rec_day_new',
            field=models.DateField(default='2020-01-01'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='reg_day_future',
            field=models.DateField(default='2020-01-01'),
        ),
    ]
