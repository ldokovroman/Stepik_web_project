from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET
from django.contrib.auth import login
from .models import Question, Answer
from .forms import AskForm, AnswerForm

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
    return render(request, "index.html", {
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
    return render(request, "popular.html", {
        "page": page,
        "paginator": paginator
    })

def question(request, id):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        form = AnswerForm()
    try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
        raise Http404
    try:
        answers = Answer.objects.filter(question=question)
    except Answer.DoesNotExist:
        answers = None
    return render(request, "question.html", {
        "question": post,
        "answers": answers,
        "form": form
    })

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, "ask.html", {
        "form": form
    })

def sign_up(request):
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = CreateUser()
    return render(request, "signup.html", {
            "form": form
    })


def test(request, *args, **kwargs):
    return HttpResponse("OK")
