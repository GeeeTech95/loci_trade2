# Generated by Django 3.0.5 on 2021-07-21 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0007_auto_20210718_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='deposit_earning',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='wallet',
            name='funded_earning',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='wallet',
            name='withdrawals',
            field=models.FloatField(default=0.0),
        ),
    ]