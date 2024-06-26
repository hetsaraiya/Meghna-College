# Generated by Django 4.2.5 on 2024-01-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_student_institute_alter_instiute_courses_provided"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="id",
        ),
        migrations.RemoveField(
            model_name="student",
            name="surname",
        ),
        migrations.AddField(
            model_name="student",
            name="course",
            field=models.CharField(
                choices=[("Bcom", "Bcom"), ("BBA", "BBA"), ("BCA", "BCA")],
                default=list,
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="student_id",
            field=models.CharField(
                max_length=20, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
