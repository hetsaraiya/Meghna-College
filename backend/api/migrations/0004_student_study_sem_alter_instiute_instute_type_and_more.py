# Generated by Django 4.2.5 on 2024-01-20 17:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_remove_student_id_remove_student_surname_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="study_sem",
            field=models.IntegerField(
                default=1,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(8),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="instiute",
            name="instute_type",
            field=models.CharField(
                choices=[
                    ("SCHOOL", "School"),
                    ("COLLEGE", "College"),
                    ("HOSTEL", "Hostel"),
                ],
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="fees_paid",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="student",
            name="fees_unpaid",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="student",
            name="gender",
            field=models.CharField(
                choices=[("Male", "Male"), ("Female", "Female")], max_length=10
            ),
        ),
    ]