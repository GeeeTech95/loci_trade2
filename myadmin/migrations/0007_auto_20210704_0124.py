# Generated by Django 3.0.5 on 2021-07-04 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0006_auto_20210703_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletaddress',
            name='address',
            field=models.CharField(help_text='enter your own wallet address for this,ensure its correct', max_length=200),
        ),
        migrations.AlterField(
            model_name='walletaddress',
            name='coin_code',
            field=models.CharField(help_text='coin code w.g BTC', max_length=15),
        ),
        migrations.AlterField(
            model_name='walletaddress',
            name='coin_name',
            field=models.CharField(help_text='full name of coin,e.g Bitcoin', max_length=30),
        ),
    ]