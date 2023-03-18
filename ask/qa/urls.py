from django.urls import path
from views import test

urlpatterns = [
    path("", test),
    path("login/", test),
    path("signup/", test),
    path("question/<int:id>/", test),
    path("ask/", test),
    path("popular/", test),
    path("new/", test)
]
