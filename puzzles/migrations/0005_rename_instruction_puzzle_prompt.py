# Generated by Django 4.2.3 on 2023-08-21 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0004_puzzle_solution_alter_puzzle_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='puzzle',
            old_name='instruction',
            new_name='prompt',
        ),
    ]
