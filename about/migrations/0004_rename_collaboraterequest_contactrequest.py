# Generated by Django 4.2.8 on 2023-12-20 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_about_profile_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CollaborateRequest',
            new_name='ContactRequest',
        ),
    ]
