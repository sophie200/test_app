# Generated by Django 3.2.2 on 2021-05-30 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporters', '0019_shirt'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='size',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]