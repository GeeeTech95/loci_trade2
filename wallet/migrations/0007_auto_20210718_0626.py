# Generated by Django 3.0.5 on 2021-07-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0006_auto_20210708_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='coin',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('WITHDRAWAL', 'WITHDRAWAL'), ('DEPOSIT', 'DEPOSIT'), ('BONUS', 'BONUS'), ('AIR DROP', 'AIR DROP'), ('REFERAL EARNING', 'REFERAL EARNING')], max_length=20),
        ),
    ]