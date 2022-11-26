from django.db import models
from django.conf import settings


TYPES = (
    ("back", "Backend"),
    ("front", "Frontend"),
    ("android", "Android"),
    ("ios", "iOS"),
)
PRIO = (("low", "Low"), ("medium", "Medium"), ("high", "High"))
TAGS = (("bug", "Bug"), ("task", "Task"), ("improvement", "Improvment"))
STATUS = (("todo", "To do"), ("in progress", "In progress"), ("close", "Close"))
PERM = (("restricted", "Contributor"), ("all", "Author"))


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TYPES, default="back")


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    permissions = models.CharField(choices=PERM, max_length=50, default="restricted")
    role = models.CharField(max_length=50)


class Issue(models.Model):

    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    tag = models.CharField(choices=TAGS, max_length=50, default="bug")
    priority = models.CharField(choices=PRIO, max_length=50, default="low")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=50, default="todo")
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author"
    )
    assignee_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="assignee"
    )
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=50)
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
