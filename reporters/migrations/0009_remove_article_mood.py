# Generated by Django 3.2.2 on 2021-05-12 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporters', '0008_delete_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='mood',
        ),
    ]