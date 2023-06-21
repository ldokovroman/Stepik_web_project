from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("qa.urls")),
    path("login/", include("qa.urls")),
    path("signup/", include("qa.urls")),
    path("question/<int:id>/", include("qa.urls")),
    path("ask/", include("qa.urls")),
    path("popular/", include("qa.urls")),
    path("new/", include("qa.urls"))
]
