# Generated by Django 5.0.3 on 2024-04-15 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_visitors_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]