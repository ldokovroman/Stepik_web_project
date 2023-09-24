from django.urls import path
from .views import main_page, question, popular, ask, sign_up, log_in, log_out

urlpatterns = [
    path("", main_page, name="main_page"),
    path("ask/", ask, name="ask"),
    path("login/", log_in, name="log_in"),
    path("logout/", log_out, name="log_out"),
    path("popular/", popular, name="popular"),
    path("question/<int:id>/", question, name="question"),
    path("signup/", sign_up, name="sign_up"),
]
