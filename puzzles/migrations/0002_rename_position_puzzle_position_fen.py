# Generated by Django 4.2.3 on 2023-07-26 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='puzzle',
            old_name='position',
            new_name='position_fen',
        ),
    ]