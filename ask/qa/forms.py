from django import forms
from django.contrib.auth.models import User
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255, label="Title", required=True)
    text = forms.CharField(widget=forms.Textarea, label="Question", required=True)

    title.widget.attrs.update({"class": "shadow border border-3 border-primary form__border col-md-8"})
    text.widget.attrs.update({"class": "shadow border border-3 border-primary form__border col-md-12", "rows": 7})

    def save(self):
        self.cleaned_data["author"] = self.user
        question = Question.objects.create(**self.cleaned_data)
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label="Your answer", required=True)
    question_id = forms.IntegerField(min_value=0)

    text.widget.attrs.update({"class": "shadow border border-3 border-primary form__border col-md-6", "rows": 5})

    def clean_question_id(self):
        question_id = self.cleaned_data["question_id"]
        try:
            question = Question.objects.get(id=question_id)
            self.question = question
        except Question.DoesNotExist:
            raise forms.ValidationError("The question doesn't exist", code="invalid")
        return question.id

    def save(self):
        answer = Answer(text=self.cleaned_data["text"], question=self.question, author=self.user)
        answer.save()
        return answer


class SignUpForm(forms.Form):
    username = forms.CharField(min_length=6, max_length=30, label="Username")
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, min_length=6, max_length=30, label="Password")

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
    username = forms.CharField(min_length=6, max_length=30, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, min_length=6, max_length=30, label="Password")
