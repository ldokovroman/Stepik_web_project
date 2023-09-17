from django import forms
from .models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=255, label="Заголовок")
    text = forms.CharField(widget=forms.Textarea, label="Текст вопроса")

    def clean_title(self):
        title = self.cleaned_data["title"]
        if not title:
            raise forms.ValidationError("Заголовок не должен быть пыстным", code="required")
        return title

    def clean_text(self):
        text = self.cleaned_data["text"]
        if not text:
            raise forms.ValidationError("Текст вопроса не должен быть пыстным", code="required")
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label="Текст ответа")
    question = forms.IntegerField(min_value=0)

    def clean_text(self):
        text = self.cleaned_data["text"]
        if not text:
            raise forms.ValidationError("Текст вопроса не должен быть пыстным", code="required")
        return text

    def clean_question(self):
        question_id = self.cleaned_data["question"]
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise forms.ValidationError("Вопроса не существует", code="invalid")
        return question.id

    def save(self):
        question = Question.objects.get(id=self.cleaned_data["question"])
        answer = Answer(text=self.cleaned_data["text"], question=question)
        answer.save()
        return answer
