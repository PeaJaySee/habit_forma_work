# Generated by Django 5.1.6 on 2025-03-19 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_progress_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
