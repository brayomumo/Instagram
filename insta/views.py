from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Image,Profile,Comment

# Create your views here.
@login_required(login_url = '/accounts/login')
def index(request):
    return render (request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required(login_url = '/accounts/login')
def profile(request):
    current_user = request.user

    images = Image.objects.filter(profile_id = current_user.id)
    return render(request, 'profile.html', {"images":images})
    

@login_required(login_url = '/accounts/login')
def user_profile(request, user_id):
    profile = Profile.objects.get(id = user_id)
    images = Image.objects.filter(user_id = user_id)
    return render(request, "profile.html", {"profile": profile, "images":images})

@login_required(login_url = '/accounts/login')
def single_post(request, image_id):
    image = Image.objects.filter(id = image_id)
    return render(request, "single_post.html", {"image":image})

    