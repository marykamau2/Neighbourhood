from django.shortcuts import redirect,render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm, BusinessForm,UpdateProfileForm, NeighbourHoodForm, PostForm
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood, Profile, Business, Post 



@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
    

# def edit_profile(request, username):
#     user = User.objects.get(username=username)
#     if request.method == 'POST':
#         form = UpdateProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('profile', user.username)
#     else:
#         form = UpdateProfileForm()
#     return render(request, 'create_profile.html', {'form': form})


# def profile(request, username):
#     return render(request, 'profile.html')


# def neighbourhoods(request):
#     all_hoods = Neighbourhood.objects.all()
#     all_hoods = all_hoods[::-1]
#     params = {
#         'all_hoods': all_hoods,
#     }
#     return render(request, 'neighbourhoods.html', params)


# def create_neighbourhood(request):
#     if request.method == 'POST':
#         form = NeighbourHoodForm(request.POST, request.FILES)
#         if form.is_valid():
#             hood = form.save(commit=False)
#             hood.admin = request.user.profile
#             hood.save()
#             return redirect('hood')
#     else:
#         form = NeighbourHoodForm()
#     return render(request, 'newhood.html', {'form': form})


# def join_neighbourhood(request, id):
#     neighbourhood = get_object_or_404(Neighbourhood, id=id)
#     request.user.profile.neighbourhood = neighbourhood
#     request.user.profile.save()
#     return redirect('hood')


# def leave_neighbourhood(request, id):
#     hood = get_object_or_404(Neighbourhood, id=id)
#     request.user.profile.neighbourhood = None
#     request.user.profile.save()
#     return redirect('hood')


# def single_neighbourhood(request, hood_id):
#     hood = Neighbourhood.objects.get(id=hood_id)
#     business = Business.objects.filter(neighbourhood=hood)
#     posts = Post.objects.filter(hood=hood)
#     posts = posts[::-1]
#     if request.method == 'POST':
#         form = BusinessForm(request.POST)
#         if form.is_valid():
#             b_form = form.save(commit=False)
#             b_form.neighbourhood = hood
#             b_form.user = request.user.profile
#             b_form.save()
#             return redirect('single-hood', hood.id)
#     else:
#         form = BusinessForm()
#     params = {
#         'hood': hood,
#         'business': business,
#         'form': form,
#         'posts': posts
#     }
#     return render(request, 'single_hood.html', params)



# def create_post(request, hood_id):
#     hood = Neighbourhood.objects.get(id=hood_id)
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.hood = hood
#             post.user = request.user.profile
#             post.save()
#             return redirect('single-hood', hood.id)
#     else:
#         form = PostForm()
#     return render(request, 'post.html', {'form': form})


