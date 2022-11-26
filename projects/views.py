from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from django.contrib.auth.models import User
from projects.models import Contributor, Issue, Project, Comment
from projects.serializers import (
    CommentSerializer,
    ContributorSerializer,
    IssueSerializer,
    ProjectSerializer,
)
from projects.permissions import (
    ProjectPermission,
    ContributorPermission,
    IssuePermission,
    CommentPermission,
)


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [ProjectPermission]

    def get_queryset(self):
        return Project.objects.all()

    def perform_create(self, serializer):
        new_project = serializer.save()
        Contributor.objects.create(
            user=self.request.user, project=new_project, permissions="all"
        )
        new_project.save()


class ContributorViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [ContributorPermission]

    def get_queryset(self):
        project = get_object_or_404(Project, pk=self.kwargs["project_id"])
        return Contributor.objects.filter(project=project)


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IssuePermission]

    def get_queryset(self):
        project = get_object_or_404(Project, pk=self.kwargs["project_id"])
        return Issue.objects.filter(project=project)

    def perform_create(self, serializer):
        project = get_object_or_404(Project, pk=self.kwargs["project_id"])
        assignee_user = get_object_or_404(User, pk=self.request.POST["assignee_user"])
        serializer.save(
            project=project, author=self.request.user, assignee_user=assignee_user
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]

    def get_queryset(self):
        issue = get_object_or_404(Issue, pk=self.kwargs["issue_id"])

        return Comment.objects.filter(issue=issue)

    def perform_create(self, serializer):

        issue = get_object_or_404(Issue, pk=self.kwargs["issue_id"])
        serializer.save(author_user=self.request.user, issue=issue)
