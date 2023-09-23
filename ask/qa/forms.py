from django import forms
from django.contrib.auth.models import User
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255, label="Title")
    text = forms.CharField(widget=forms.Textarea, label="Question")

    def clean_title(self):
        title = self.cleaned_data["title"]
        if not title:
            raise forms.ValidationError("The title mustn't be empty", code="required")
        return title

    def clean_text(self):
        text = self.cleaned_data["text"]
        if not text:
            raise forms.ValidationError("The question text mustn't be empty", code="required")
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label="Your answer")
    question = forms.IntegerField(min_value=0)

    def clean_text(self):
        text = self.cleaned_data["text"]
        if not text:
            raise forms.ValidationError("The answer text mustn't be empty", code="required")
        return text

    def clean_question(self):
        question_id = self.cleaned_data["question"]
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise forms.ValidationError("The question doesn't exist", code="invalid")
        return question.id

    def save(self):
        question = Question.objects.get(id=self.cleaned_data["question"])
        answer = Answer(text=self.cleaned_data["text"], question=question)
        answer.save()
        return answer


class SignUpFrom(forms.Form):
    username = forms.CharField(min_length=6, max_length=30, label="Username", required=True)
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, min_length=6, max_length=30, label="Password", required=True)

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).count():
            raise forms.ValidationError("The specified username already exists, please enter a different one!", code="unique")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).count():
            raise forms.ValidationError("The specified email already exists, please enter a different one!", code="unique")
        return email

    def save(self):
        user = User.objects.create_user(username=self.cleaned_data["username"],
                                        email=self.cleaned_data["email"],
                                        password=self.cleaned_data["password"])
        return user


class LoginForm(forms.Form):
    username = forms.CharField(min_length=6, max_length=30, label="Username", required=True)
    password = forms.CharField(widget=forms.PasswordInput, min_length=6, max_length=30, label="Password", required=True)
