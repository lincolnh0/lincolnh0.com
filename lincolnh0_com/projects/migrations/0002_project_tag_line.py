# Generated by Django 3.1.13 on 2021-11-07 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="tag_line",
            field=models.CharField(default="", max_length=200),
        ),
    ]
