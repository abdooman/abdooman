# Generated by Django 4.1.5 on 2023-01-14 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='birth_date',
            new_name='birthdate',
        ),
    ]
