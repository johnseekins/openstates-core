# Generated by Django 3.1.7 on 2021-04-02 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0031_auto_20210401_1449"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="dedupe_key",
            field=models.CharField(max_length=500, null=True),
        ),
    ]
