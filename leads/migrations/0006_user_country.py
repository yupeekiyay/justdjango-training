# Generated by Django 3.1.7 on 2021-02-25 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_lead_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]