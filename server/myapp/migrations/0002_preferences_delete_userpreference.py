# Generated by Django 5.1.4 on 2024-12-23 02:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_duration', models.PositiveIntegerField(default=25)),
                ('short_break_duration', models.PositiveIntegerField(default=5)),
                ('long_break_duration', models.PositiveIntegerField(default=15)),
                ('long_break_interval', models.PositiveIntegerField(default=4)),
                ('theme', models.CharField(default='default', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserPreference',
        ),
    ]
