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
            raise forms.ValidationError("Текст аопроса не должен быть пыстным", code="required")
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
