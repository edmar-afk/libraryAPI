# Generated by Django 5.0.3 on 2024-03-30 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_librarian_site'),
    ]

    operations = [
        migrations.RenameField(
            model_name='librarian',
            old_name='is_librarian',
            new_name='is_librarian_head',
        ),
        migrations.AddField(
            model_name='librarian',
            name='position',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
