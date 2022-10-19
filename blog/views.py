# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm 
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Home Blog
from blog.forms import PostCreateForm, CategoryCreateForm, UserCreateForm
from blog.models import Post, Category, Profile


def index(request):
    last_posts = Post.objects.all().order_by('-created', 'title')[:5]
    return render(request, 'home.html', {'last_posts': last_posts})


# Posts: List, Show, Create, Edit, Delete
def post_list(request):
    posts = Post.objects.all().order_by('-created', 'title')
    return render(request, 'posts/list.html', {'posts': posts})


def post_show(request, pk: int):
    post = Post.objects.get(pk=pk)
    return render(request, "posts/show.html", {'post': post})


def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post.list')

    return render(request, 'posts/create.html', {'form': PostCreateForm})


def post_edit(request):
    pass


def post_delete(request):
    pass


# Categories: List, Show, Create, Edit, Delete
def category_list(request):
    categories = Category.objects.all().order_by('-name')
    return render(request, 'categories/list.html', {'categories': categories})


def category_create(request):
    if request.method == "POST":
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/categories/listar')

    return render(request, 'categories/create.html', {'form': CategoryCreateForm})


def category_edit(request):
    pass


def category_delete(request):
    pass


# Profile: List, Show, Create, Edit, Delete
def profile_list(request):
    profiles = Profile.objects.select_related()
    return render(request, 'profiles/list.html', {'profiles': profiles})


def profile_show(request, pk: int):
    profile = Profile.objects.get(pk=pk)
    return render(request, "profiles/show.html", {'profile': profile})


def profile_edit(request):
    return HttpResponse("Editar perfil del usuario")


# User
def user_create(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    return render(request, 'users/create.html', {'form': UserCreateForm})


# Authentication
def auth_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')

    return render(request, 'auth/login.html', {'form': AuthenticationForm()})


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#prueba de registro
def register_request(request):
	if request.method == "POST":
		form = UserCreateForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = UserCreateForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})