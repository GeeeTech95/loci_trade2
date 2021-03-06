# Generated by Django 3.0.5 on 2021-07-04 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_remove_wallet_preferred_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='duration',
            field=models.PositiveIntegerField(help_text='plan duration in days'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='interest_rate',
            field=models.FloatField(help_text='in %,e.g 50,100,200'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='max_cost',
            field=models.FloatField(blank=True, help_text='maximum investment for thie plan,currency is USD', null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='min_cost',
            field=models.FloatField(help_text='minimum investment for thie plan,currency is USD'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(help_text='name you wish to call the investment plan', max_length=40),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wallet_subscribers', to='wallet.Plan'),
        ),
    ]
