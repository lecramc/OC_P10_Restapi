from projects.views import (
    ProjectViewSet,
    ContributorViewSet,
    IssueViewSet,
    CommentViewSet,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r"projects", ProjectViewSet, basename="project")
router.register(
    r"projects/(?P<project_id>[^/.]+)/users", ContributorViewSet, basename="user"
)
router.register(
    r"projects/(?P<project_id>[^/.]+)/issues", IssueViewSet, basename="issue"
)
router.register(
    r"projects/(?P<project_id>[^/.]+)/issues/(?P<issue_id>[^/.]+)/comments",
    CommentViewSet,
    basename="comment",
)
urlpatterns = router.urls
