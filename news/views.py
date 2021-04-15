from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from .forms import CommentForm, PostForm
from .models import Post, Comment, Author
from home_page.models import Application, WelcomeWords, MissionVision, Slider, HeadingOne, HeadingTwo, HeadingThree
from about.models import Director, AboutUs, TeamDescription, Team
from gallery.models import GallerySlider, Gallery, GalleryExtra
from subscription.models import Signup
from muslim_school.models import  Sliding, HeaderOne, HeaderTwo, ApplicationForm, Welcome, Achievers, Staff
from online_library.models import Library
from Projects.models import Project
from admission.models import Admission, Fees, Uniform
from letters.models import Letters
from family.models import Family


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) 
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_results.html', context)



def get_category_count():
    queryset = Post \
        .objects \
        .values('Categories__title') \
        .annotate(Count('Categories__title'))
    return queryset

def index(request):
    featured = Post.objects.filter(featured=True)
    most_recent = Post.objects.order_by('-timestamp')[:3]
    recent_projects = Project.objects.order_by('-timestamp')[:3]

    application = Application.objects.all()
    welcome_words = WelcomeWords.objects.all()
    mission_vision = MissionVision.objects.all()
    
    slider = Slider.objects.all()

    heading_one = HeadingOne.objects.all()
    heading_two = HeadingTwo.objects.all()
    heading_three = HeadingThree.objects.all()

    context = {
        'object_list': featured,
        'application' : application ,
        'welcome_words' : welcome_words ,
        'mission_vision' : mission_vision ,
        'most_recent': most_recent,
        'slider' : slider,
        'heading_one' : heading_one,
        'heading_two' : heading_two,
        'heading_three': heading_three,
        'recent_projects': recent_projects,
    }
    return render(request, 'index.html', context)


def blog(request):

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:4]
    post_list = Post.objects.order_by('-timestamp')

    paginator = Paginator(post_list, 5)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)


    context = {
        'queryset' : paginated_queryset,
        'page_request_var': page_request_var,
        'most_recent': most_recent,
        'category_count': category_count,
    }
    return render(request, 'blog.html', context)

def post(request, id):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:4]

    post = get_object_or_404(Post, id=id)

    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, user=request.user, content=content, reply=comment_qs)
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'most_recent': most_recent,
        'category_count': category_count,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'post.html', context)

def about(request):
    most_recent = Post.objects.order_by('-timestamp')[:4]
    director = Director.objects.all()
    about_us = AboutUs.objects.all()
    team_description = TeamDescription.objects.all()
    team = Team.objects.all()
    
    context = {
        'director': director,
        'about_us' : about_us, 
        'team_description' : team_description,
        'team': team,
        'most_recent': most_recent,
        
    }
    return render(request, 'about.html', context)

def gallery(request):
    gallery_slider = GallerySlider.objects.order_by('-timestamp')
    gallery = Gallery.objects.order_by('-timestamp')
    gallery_extra = GalleryExtra.objects.order_by('-timestamp')

    context = {
        'gallery_slider' : gallery_slider,
        'gallery' : gallery,
        'gallery_extra' : gallery_extra,
        
    }
    return render(request, 'gallery.html', context)

def post_create(request):
    title = 'Create'
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "post_create.html", context)

def post_update(request, id):
    title = 'Update'
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "post_create.html", context)

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse("post-list"))

def madrassah(request):
    application_form = ApplicationForm.objects.all()
    welcome = Welcome.objects.all()
    sliding = Sliding.objects.all()

    header_one = HeaderOne.objects.all()
    header_two = HeaderTwo.objects.all()

    achievers = Achievers.objects.all()
    staff = Staff.objects.all()

    context = {
        'application_form' : application_form ,
        'welcome' : welcome ,
        'sliding' : sliding,
        'header_one' : header_one,
        'header_two' : header_two,
        'achievers': achievers,
        'staff': staff,
    }
    return render(request, 'madrassah.html', context)


def library(request):
    library_list = Library.objects.order_by('-timestamp')

    paginator = Paginator(library_list, 8)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)


    context = {
        'queryset' : paginated_queryset,
        'page_request_var': page_request_var,

    }
    return render(request, 'library.html', context)


def library_detail(request, id):
    library_detail = get_object_or_404(Library, id=id)

    context = {
        'library_detail': library_detail,
        
    }
    return render(request, 'library_detail.html', context)


def project_list(request):
    project_list = Project.objects.order_by('-timestamp')

    paginator = Paginator(project_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)


    context = {
        'queryset' : paginated_queryset,
        'page_request_var': page_request_var,

    }
    return render(request, 'project_list.html', context)

def project_detail(request, id):
    project_detail = get_object_or_404(Project, id=id)

    context = {
        'project_detail': project_detail,
        
    }
    return render(request, 'project_detail.html', context)


def admission(request):
    admission = Admission.objects.all()
    fees = Fees.objects.all()
    uniform = Uniform.objects.all()
   
    
    context = {
        'admission': admission,
        'fees' : fees, 
        'uniform' : uniform,
        
    }
    return render(request, 'admission.html', context)



def letters(request):
    letters = Letters.objects.order_by('-timestamp')

    context = {
        'letters': letters,
            
    }
    return render(request, 'letters.html', context)    


def family(request):
    family = Family.objects.all()
   
    context = {
        'family': family,
        
    }
    return render(request, 'team.html', context)

