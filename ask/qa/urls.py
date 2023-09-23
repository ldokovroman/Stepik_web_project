from django.urls import path
from .views import main_page, test, question, popular, ask, sign_up

urlpatterns = [
    path("", main_page, name="main_page"),
    path("login/", test),
    path("signup/", sign_up, name="sign_up"),
    path("question/<int:id>/", question, name="question"),
    path("ask/", ask, name="ask"),
    path("popular/", popular, name="popular"),
]
