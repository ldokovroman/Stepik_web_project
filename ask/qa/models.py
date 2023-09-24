from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name="likes")
    objects = QuestionManager()

    def get_url(self):
        return reverse("question", args=(self.id,))

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
