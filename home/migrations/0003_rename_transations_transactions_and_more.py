# Generated by Django 5.1.3 on 2024-11-26 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_transations'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transations',
            new_name='Transactions',
        ),
        migrations.RenameField(
            model_name='transactions',
            old_name='transations_type',
            new_name='transactions_type',
        ),
    ]
