# Generated by Django 4.1.1 on 2022-11-18 09:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.UUIDField(editable=False, primary_key=True, serialize=False, verbose_name=uuid.UUID('f8423da5-abaf-48ec-8824-c6a265999977')),
        ),
    ]