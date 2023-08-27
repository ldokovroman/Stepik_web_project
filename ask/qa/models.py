from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):

    def new(self):
        return self.order_by("-added_at")

    def popular(self):
        return self.order_by("-rating")

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, null=True, related_name="users_likes_details")
    objects = QuestionManager()

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
