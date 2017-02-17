from urllib.parse import quote_plus
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm
from .models import Post
from django.db.models import Q

# Create your views here.


def post_list(request):
    queryset_list = Post.objects.active()  #.order_by("-Updated")
    today = timezone.now().date()
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(Title__icontains=query) |
            Q(Content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 5)  # Show 25 contacts per page
    page_request_val = 'list'
    page = request.GET.get(page_request_val)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "title" : "Hello, ",
        "data" : "This is from index data",
        "object_list" : queryset,
        "page_request_val":page_request_val,
        "today":today,
    }
    return render(request, 'list.html', context)


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    if not request.user.is_authenticated():
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request,"Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, 'forms.html', context)

def post_detail(request,slug = None):
    instance = get_object_or_404(Post, slug = slug)
    if instance.draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    share_string = quote_plus(instance.Content)
    context = {
        "title" : instance.Title,
        "instance":instance,
        "share_string": share_string,
    }
    return render(request, 'details.html', context)

def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        messages.success(request,"Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.Title,
        "instance": instance,
        "form":form,
    }
    return render(request, 'forms.html', context)

def post_delete(request,slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post,slug=slug)
    instance.delete()
    messages.success(request,"Post Deleted")
    return redirect("posts:list")

