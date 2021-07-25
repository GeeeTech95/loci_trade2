# Generated by Django 3.0.5 on 2021-07-08 11:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_auto_20210704_0147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallet',
            old_name='set_amount',
            new_name='bonus_amount',
        ),
        migrations.AddField(
            model_name='pendingdeposit',
            name='decline_reason',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pendingdeposit',
            name='is_declined',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wallet',
            name='wallet_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]