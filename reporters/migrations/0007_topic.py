# Generated by Django 3.2.2 on 2021-05-12 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporters', '0006_rename_essay_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('specificity', models.CharField(max_length=100)),
            ],
        ),
    ]