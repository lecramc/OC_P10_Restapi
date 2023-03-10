# Generated by Django 4.1.2 on 2022-11-10 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_remove_issue_satus_issue_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="type",
            field=models.CharField(
                choices=[
                    ("back", "Backend"),
                    ("front", "Frontend"),
                    ("android", "Android"),
                    ("ios", "iOS"),
                ],
                default="back",
                max_length=50,
            ),
        ),
    ]
