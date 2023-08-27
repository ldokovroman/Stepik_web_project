from django.urls import path
from .views import *

urlpatterns = [
    path("", main_page, name="main_page"),
    path("login/", test),
    path("signup/", test),
    path("question/<int:id>/", question, name="question"),
    path("ask/", test),
    path("popular/", popular, name="popular"),
    path("new/", test)
]
