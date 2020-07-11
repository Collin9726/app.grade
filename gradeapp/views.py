from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .email import send_signup_email
from .forms import NewProfileForm, NewProjectForm
from .models import Profile, Project



def index(request):     
    projects =  Project.objects.order_by("-posted")
    title = 'Home'
    return render(request, 'home.html', {"title": title, "projects": projects})

@login_required(login_url='/accounts/login/')
def send_email(request):
    current_user = request.user
    email = current_user.email
    name = current_user.username
    send_signup_email(name, email)
    return redirect(create_profile)


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.account_holder = current_user
            profile.save()
        return redirect(my_profile)

    else:
        form = NewProfileForm()
    
    title = "Create profile"
    return render(request, 'create-profile.html', {"form": form, "title": title})


@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user = request.user
    try:
        profile = Profile.objects.get(account_holder = current_user)
    except Profile.DoesNotExist:
        return redirect(create_profile)

    title = profile.account_holder.username
    return render(request, 'my-profile.html', {"profile": profile, "title": title})


@login_required(login_url='/accounts/login/')
def change_profile_photo(request):
    current_user = request.user
    try:
        profile = Profile.objects.get(account_holder = current_user)
    except Profile.DoesNotExist:
        raise Http404()
    
    if request.method == 'POST':
        profile.profile_photo = request.FILES['img']        
        profile.update_profile()
        return redirect(my_profile)

    title = "Profile photo"    
    return render(request, 'update-prof-pic.html', {"title": title})


@login_required(login_url='/accounts/login/')
def delete_profile(request):
    current_user = request.user
    try:
        profile = Profile.objects.get(account_holder = current_user)
    except Profile.DoesNotExist:
        raise Http404()

    profile.delete_profile()
    current_user.delete()
    
    return redirect(index)


@login_required(login_url='/accounts/login/')
def upload_project(request):
    current_user = request.user
    try:
        profile = Profile.objects.get(account_holder = current_user)
    except Profile.DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            this_project = form.save(commit=False)
            this_project.profile = profile
            this_project.save()
        return HttpResponseRedirect('/')

    else:
        form = NewProjectForm()

    title = "Upload Project"
    return render(request, 'upload-project.html', {"form": form, "title": title})