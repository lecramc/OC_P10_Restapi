# Generated by Django 4.1.2 on 2023-03-08 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0006_project_author_alter_contributor_permissions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="author_user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="issue",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="projects.issue",
            ),
        ),
        migrations.AlterField(
            model_name="contributor",
            name="project",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="projects.project",
            ),
        ),
        migrations.AlterField(
            model_name="issue",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="author",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="project_author",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
