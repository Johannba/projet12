# Generated by Django 4.1.5 on 2023-01-14 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0002_alter_event_event_status"),
    ]

    operations = [
        migrations.DeleteModel(name="EventStatus",),
    ]
