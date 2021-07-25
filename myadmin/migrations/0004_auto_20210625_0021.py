# Generated by Django 3.0.5 on 2021-06-25 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0003_myadmin_total_revenue'),
    ]

    operations = [
        migrations.AddField(
            model_name='myadmin',
            name='enable_verification_registration',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myadmin',
            name='points',
            field=models.FloatField(default=0.0),
        ),
    ]