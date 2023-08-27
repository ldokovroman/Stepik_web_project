from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET
from .models import Question, Answer

@require_GET
def main_page(request):
    limit = 10
    try:
        page_num = int(request.GET.get("page", 1))
    except ValueError:
        raise Http404
    questions = Question.objects.new()
    paginator = Paginator(questions, limit)
    paginator.baseurl = "/?page="
    if page_num > paginator.num_pages or page_num < 1:
        raise Http404
    page = paginator.page(page_num)
    return render(request, "main/templates/index.html", {
        "page": page,
        "paginator": paginator
    })

@require_GET
def popular(request):
    limit = 10
    try:
        page_num = int(request.GET.get("page", 1))
    except ValueError:
        raise Http404
    questions = Question.objects.popular()
    paginator = Paginator(questions, limit)
    paginator.baseurl = reverse("popular") + "?page="
    if page_num > paginator.num_pages or page_num < 1:
        raise Http404
    page = paginator.page(page_num)
    return render(request, "popular/templates/popular.html", {
        "page": page,
        "paginator": paginator
    })

@require_GET
def question(request, id):
    try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
        raise Http404
    try:
        answers = Answer.objects.filter(question=question)
    except Answer.DoesNotExist:
        answers = None
    return render(request, "question/templates/question.html", {
        "question": post,
        "answers": answers
    })

def test(request, *args, **kwargs):
    return HttpResponse("OK")
