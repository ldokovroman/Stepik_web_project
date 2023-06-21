from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET
from models import Question, Answer

@require_GET
def main_page(request):
    limit = 10
    try:
        page = int(request.GET.get("page", 1))
    except ValueError:
        raise Http404
    pages = Question.objects.new()
    paginator = Paginator(pages, limit)
    paginator.baseurl = "/?page="
    if page > paginator.num_pages or page < 1:
        raise Http404
    page = paginator.page(page)
    return render(request, "main/index.html", {
        "page": page,
        "paginator": paginator
    })

@require_GET
def popular(request):
    limit = 10
    try:
        page = int(request.GET.get("page", 1))
    except ValueError:
        raise Http404
    pages = Question.objects.popular()
    paginator = Paginator(pages, limit)
    paginator.baseurl = reverse("popular") + "?page="
    if page > paginator.num_pages or page < 1:
        raise Http404
    page = paginator.page(page)
    return render(request, "popular/popular.html", {
        "page": page,
        "paginator": paginator
    })

@require_GET
def question(request, id):
    try:
        post = Question.objects.get(id=id)
    except Question.DoesNotExist:
        raise Http404
    try:
        answers = Answer.objects.filter(question=post)[:]
    except Answer.DoesNotExist:
        answers = None
    return render(request, "question/question.html", {
        "question": post,
        "answers": answers
    })

def test(request, *args, **kwargs):
    return HttpResponse("OK")
