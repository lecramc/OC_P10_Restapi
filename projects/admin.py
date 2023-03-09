from django.contrib import admin

from .models import Project, Issue, Comment, Contributor

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    pass
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    pass