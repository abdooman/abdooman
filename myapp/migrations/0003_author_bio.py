# Generated by Django 4.1.5 on 2023-01-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_birth_date_author_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]
