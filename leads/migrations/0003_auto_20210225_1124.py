# Generated by Django 3.1.7 on 2021-02-25 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20210224_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_organizer',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]