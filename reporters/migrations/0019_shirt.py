# Generated by Django 3.2.2 on 2021-05-30 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporters', '0018_auto_20210513_0250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
            ],
        ),
    ]