# Generated by Django 3.2.9 on 2021-11-02 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='test',
            new_name='text',
        ),
    ]