# Generated by Django 3.0.5 on 2021-08-07 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0011_auto_20210807_0907'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-date']},
        ),
    ]
