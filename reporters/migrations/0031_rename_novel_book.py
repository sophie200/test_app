# Generated by Django 3.2.2 on 2021-05-30 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporters', '0030_delete_book'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Novel',
            new_name='Book',
        ),
    ]