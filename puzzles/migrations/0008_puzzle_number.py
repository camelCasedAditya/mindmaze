# Generated by Django 4.2.3 on 2023-10-19 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0007_alter_puzzle_term'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]