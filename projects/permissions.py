from rest_framework import permissions

from projects.models import Issue, Contributor


class ProjectPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ["PATCH", "PUT", "DELETE"]:
            return request.user == obj.author


class IssuePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        contributor = Contributor.objects.filter(project=view.kwargs["project_id"])
        contributors_ids = [c.pk for c in contributor]
        return request.user in contributors_ids

    def has_object_permission(self, request, view, obj):
        if request.method in ["PATCH", "PUT", "DELETE"]:
            return request.user == obj.author


class CommentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        issue = Issue.objects.get(pk=view.kwargs["issue_id"])
        if request.method in ["POST", "GET"]:
            contributor = Contributor.objects.filter(project=view.kwargs["project_id"])
            contributors_ids = [c.pk for c in contributor]
            return request.user in contributors_ids
        elif request.method in ["PUT", "DELETE", "PATCH"]:
            author = Contributor.objects.filter(
                project=view.kwargs["project_id"], permissions="all"
            )
            author_ids = [a.pk for a in author]
            return request.user in author_ids or request.user == issue.author


class ContributorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        authors = Contributor.objects.filter(project=view.kwargs["project_id"])
        author_ids = [a.pk for a in authors]
        return request.user in author_ids
