# Generated by Django 4.2.5 on 2024-01-20 18:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0007_rename_instiute_name_instiute_institute_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="instiute",
            name="courses_provided",
        ),
    ]