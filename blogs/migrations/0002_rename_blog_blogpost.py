# Generated by Django 5.0.3 on 2024-03-18 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='BlogPost',
        ),
    ]
