from projects.models import Project, Contributor, Comment, Issue
from rest_framework.serializers import ModelSerializer


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = "__all__"


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "desc",
            "tag",
            "priority",
            "project_id",
            "status",
            "author",
            "assignee_user",
        ]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["description"]
