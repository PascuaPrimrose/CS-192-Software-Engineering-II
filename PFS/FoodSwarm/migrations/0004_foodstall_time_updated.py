# Generated by Django 2.1.5 on 2019-02-09 15:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FoodSwarm', '0003_auto_20190209_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodstall',
            name='time_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
