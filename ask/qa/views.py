from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth import login, authenticate, logout, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Question, Answer
from .forms import AskForm, AnswerForm, SignUpForm, LoginForm

LIMIT = 10

@require_GET
def main_page(request):
    user = get_user(request)
    try:
        page_num = int(request.GET.get("page", 1))
    except ValueError:
        raise Http404
    questions = Question.objects.new()
    paginator = Paginator(questions, LIMIT)
    if page_num > paginator.num_pages or page_num < 1:
        raise Http404
    page = paginator.page(page_num)
    return render(request, "index.html", {
        "page": page,
        "paginator": paginator,
        "user": user
    })

@require_GET
def popular(request):
    user = get_user(request)
    try:
        page_num = int(request.GET.get("page", 1))
    except ValueError:
        raise Http404
    questions = Question.objects.popular()
    paginator = Paginator(questions, LIMIT)
    if page_num > paginator.num_pages or page_num < 1:
        raise Http404
    page = paginator.page(page_num)
    return render(request, "popular.html", {
        "page": page,
        "paginator": paginator,
        "user": user
    })

def question(request, question_id):
    user = get_user(request)
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404
    if request.method == "POST":
        if user.id is None:
            return HttpResponseRedirect(reverse("log_in"))
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.user = user
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        form = AnswerForm()
        question.rating += 1
        question.save()
    answers = question.answers.all()
    return render(request, "question.html", {
        "question": question,
        "answers": answers,
        "form": form,
        "user": user
    })

def ask(request):
    user = get_user(request)
    if user.id is None:
        return HttpResponseRedirect(reverse("log_in"))
    if user.id and request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form.user = user
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, "ask.html", {
        "form": form,
    })

def sign_up(request):
    user = get_user(request)
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse("main_page"))
    else:
        form = SignUpForm()
    return render(request, "signup.html", {
        "form": form,
        "user": user
    })

def log_in(request):
    user = get_user(request)
    login_error = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST["username"], password=request.POST["password"])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("main_page"))
            else:
                login_error = "Username or password is incorrect!"
    else:
        form = LoginForm()
    return render(request, "login.html", {
        "form": form,
        "login_error": login_error,
        "user": user
    })

@require_POST
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("log_in"))

@login_required
def delete_question(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404
    question.delete()
    return HttpResponseRedirect(reverse("main_page"))
