from django.urls import include, path
from django.contrib import admin


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("projects.urls")),
    path("auth/", include("authentication.urls")),
]
