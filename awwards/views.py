from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from django.contrib.auth import login, authenticate




# Create your views here.
def home(request):
    screenshots = Project.objects.all()
    current_user = request.user
    w= Profile.objects.all()
    return render(request, 'home.html',locals())




@login_required(login_url='/accounts/login/')
def upload_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.save()
            return redirect('home')
    else:
        form = ProjectForm()


    return render(request,'upload_project.html',locals())


def search_results(request):
    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET.get('project')
        searched_project = Project.search_by_project(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',locals())

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})



@login_required(login_url='/accounts/login/')
def profile(request, username):

    profile = User.objects.get(username=username)
    print(profile.id)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    user = request.user
    profile = User.objects.get(username=username)
    project = Project.objects.filter(owner=user)
    title = f'@{profile.username} awwward projects and screenshots'

    return render(request, 'profile.html', locals())

def project(request, project_id):
    try:
        project = Project.objects.get(id = project_id)
        rating = round(((project.design + project.usability + project.content) / 3), 2)
        if request.method == 'POST':
            form = VoteForm(request.POST)
            if form.is_valid:
                if project.design == 1:
                    project.design = int(request.POST['design'])
                else:
                    project.design = (project.design + int(request.POST['design'])) / 2
                if project.usability == 1:
                    project.usability = int(request.POST['usability'])
                else:
                    project.usability = (project.design + int(request.POST['usability'])) / 2
                if project.content == 1:
                    project.content = int(request.POST['content'])
                else:
                    project.content = (project.design + int(request.POST['content'])) / 2
                project.save()
        else:
            form = VoteForm()
    except DoesNotExist:
        raise Http404()
    return render(request,"project.html", {'form': form, 'project': project})

def edit(request):
    profile = User.objects.get(username=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('update_profile')
    else:
        form = ProfileForm()
    return render(request, 'edit_profile.html', locals())
