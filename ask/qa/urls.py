from django.urls import path
from .views import main_page, test, question, popular, ask

urlpatterns = [
    path("", main_page, name="main_page"),
    path("login/", test),
    path("signup/", test),
    path("question/<int:id>/", question, name="question"),
    path("ask/", ask, name="ask"),
    path("popular/", popular, name="popular"),
]
