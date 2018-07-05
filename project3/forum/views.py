from .models import Topics, Sections, Posts
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import RegisterForm, LoginForm, ModifyForm, AddPostForm, AddTopicForm, AddSectionForm, ModifyEmail, ModifyPassword
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='http://localhost:8000/forum/login')
def sections(request):

    all_sections = Sections.objects.all()

    context = {
        'title': 'Lista sekcji:',
        'sections': all_sections
    }

    return render(request, 'forum/sections.html', context)


@login_required(login_url='http://localhost:8000/forum/login')
def topics(request, id):

    section = Sections.objects.get(id=id)
    all_topics = Topics.objects.filter(section=section)

    context = {
        'title': 'Tematy w sekcji',
        'topics': all_topics,
        'section': section
    }

    return render(request, 'forum/topics.html', context)


@login_required(login_url='http://localhost:8000/forum/login')
def posts(request, id):

    topic = Topics.objects.get(id=id)
    all_posts = Posts.objects.filter(topic=topic)

    context = {
        'title': 'Posty w temacie',
        'posts': all_posts,
        'topic': topic
    }

    return render(request, 'forum/posts.html', context)


@login_required(login_url='http://localhost:8000/forum/login')
def details(request, id):

    post = Posts.objects.get(id=id)

    context = {
        'post': post
    }

    return render(request, 'forum/details.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            new_user.set_password(password)
            new_user.save()

            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('http://localhost:8000/forum/sections')
        else:
            render(request, 'forum/register.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'forum/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('http://localhost:8000/forum/sections')
        else:
            form = LoginForm()
            messages.info(request, 'Wrong username or password.')
            return render(request, 'forum/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'forum/login.html', {'form': form})


@login_required(login_url='http://localhost:8000/forum/login')
def modify(request, id):

    post = Posts.objects.get(id=id)

    if post.author.username == request.user.username or request.user.is_superuser:
        if request.method == 'POST':
            body = request.POST['body']
            post.body = body
            post.save()
            return redirect('http://localhost:8000/forum/details/' + id)
        else:
            form = ModifyForm()
            return render(request, 'forum/modify.html', {'form': form})
    else:
        messages.info(request, 'Nie mozesz tego modyfikowac.')
        return redirect('http://localhost:8000/forum/details/' + id)


@login_required(login_url='http://localhost:8000/forum/login')
def delete(request, id):

    post = Posts.objects.get(id=id)
    tmp = str(post.topic.id)

    if post.author.username == request.user.username or request.user.is_superuser:
        post.delete()
        return redirect('http://localhost:8000/forum/posts/' + tmp)
    else:
        messages.info(request, "Nie mozesz tego usunac.")
        return redirect('http://localhost:8000/forum/details/' + id)


@login_required(login_url='http://localhost:8000/forum/login')
def add_post(request, id):

    topic = Topics.objects.get(id=id)

    if request.method == 'POST':
        body = request.POST['body']
        new_post = Posts(topic=topic, author=request.user, body=body)
        new_post.save()
        return redirect('http://localhost:8000/forum/posts/' + str(topic.id))
    else:
        form = AddPostForm()
    return render(request, 'forum/add_post.html', {'form': form})


@login_required(login_url='http://localhost:8000/forum/login')
def delete_topic(request, id):

    topic = Topics.objects.get(id=id)
    tmp = str(topic.section.id)
    topic.delete()
    return redirect('http://localhost:8000/forum/topics/' + tmp)


@login_required(login_url='http://localhost:8000/forum/login')
def add_topic(request, id):

    section = Sections.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST['title']
        new_topic = Topics(section=section, author=request.user, title=title)
        new_topic.save()
        return redirect('http://localhost:8000/forum/topics/' + str(section.id))
    else:
        form = AddTopicForm()
    return render(request, 'forum/add_topic.html', {'form': form})


@login_required(login_url='http://localhost:8000/forum/login')
def add_section(request):

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        new_section = Sections(title=title, description=description)
        new_section.save()
        return redirect('http://localhost:8000/forum/sections')
    else:
        form = AddSectionForm()
    return render(request, 'forum/add_section.html', {'form': form})


@login_required(login_url='http://localhost:8000/forum/login')
def modify_profile(request):

    context = {
        'title': 'Twoj profil:',
        'user': request.user
    }

    return render(request, 'forum/modify_profile.html', context)


@login_required(login_url='http://localhost:8000/forum/login')
def modify_password(request):

    if request.method == 'POST':
        password = request.POST['password']
        request.user.set_password(password)
        request.user.save()
        messages.info(request, "Haslo zmienione.")
        return redirect('http://localhost:8000/forum/profile')
    else:
        form = ModifyPassword()
    return render(request, 'forum/modify_password.html', {'form': form})


@login_required(login_url='http://localhost:8000/forum/login')
def modify_email(request):

    if request.method == 'POST':
        email = request.POST['email']
        request.user.email = email
        request.user.save()
        messages.info(request, "Email zmieniony.")
        return redirect('http://localhost:8000/forum/profile')
    else:
        form = ModifyEmail()
    return render(request, 'forum/modify_email.html', {'form': form})