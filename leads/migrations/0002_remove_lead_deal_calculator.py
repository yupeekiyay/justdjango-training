# Generated by Django 3.1.7 on 2021-02-23 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='deal_calculator',
        ),
    ]
