# Generated by Django 4.1.5 on 2023-01-25 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0013_alter_orderdetails_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderdetails',
            options={'verbose_name_plural': 'Order Details'},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='created_at',
            new_name='transaction_time',
        ),
    ]
