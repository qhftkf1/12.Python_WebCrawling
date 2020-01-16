from django.shortcuts import render
from django_crawl.models import BlogData
from django.shortcuts import redirect

from django.core import serializers
from django.http import HttpResponse
from .forms import PostForm
# Create your views here.
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            return render(request, 'post_edit.html', {'form' : form})
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form' : form})

def index(request):
    crawl_data_count = BlogData.objects.all().count()
    crawl_data_all = BlogData.objects.all()

    context = {
        'crawl_data_count':crawl_data_count,
        'crawl_data_all':crawl_data_all,
    }

    return render(request, 'index.html', context=context)

def find(request):
    crawl_data_count = BlogData.objects.all().count()
    crawl_data_all = BlogData.objects.all()
    crawl_list = serializers.serialize('json', crawl_data_all)

    context = {
        'crawl_data_count':crawl_data_count,
        'crawl_data_all':crawl_data_all,
    }
    # return HttpResponse(crawl_list, content_type="text/json-comment-filtered")
    return render(request, 'find.html', context=context)

def delete(request):
    BlogData.objects.all().delete()
    return redirect('/')
