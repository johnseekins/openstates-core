# Generated by Django 3.0.5 on 2020-09-14 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0024_auto_20200914_1101"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="billdocumentlink",
            name="text",
        ),
        migrations.RemoveField(
            model_name="billversionlink",
            name="text",
        ),
        migrations.RemoveField(
            model_name="eventagendamedialink",
            name="text",
        ),
        migrations.RemoveField(
            model_name="eventdocumentlink",
            name="text",
        ),
        migrations.RemoveField(
            model_name="eventmedialink",
            name="text",
        ),
    ]
