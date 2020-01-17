from django.shortcuts import render
from django_crawl.models import BlogData
from django.shortcuts import redirect

from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django_crawl.forms import PostForm
# Create your views here.
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             search_instance = form.cleaned_data['search_data']
#             return HttpResponse()
#     else:
#         form = PostForm()
#     return render(request, 'post_edit.html', {'form' : form})

def index(request):
    crawl_data_count = BlogData.objects.all().count()
    crawl_data_all = BlogData.objects.all()
    crawl_data_job = BlogData.objects.filter(tag="job_general")
    context = {
        'crawl_data_count':crawl_data_count,
        'crawl_data_all':crawl_data_all,
        'crawl_data_job':crawl_data_job,
    }

    return render(request, 'index.html', context=context)

def job(request):
    crawl_data_job = BlogData.objects.filter(tag="job_general")
    context = {
        'crawl_data_job':crawl_data_job,
    }
    return render(request, 'job_page.html', context=context)
def future(request):
    crawl_data_future = BlogData.objects.filter(tag="future")
    context = {
        'crawl_data_future':crawl_data_future,
    }
    return render(request, 'future_page.html', context=context)
def pknu(request):
    crawl_data_pknu = BlogData.objects.filter(tag="pknu")
    context = {
        'crawl_data_pknu':crawl_data_pknu,
    }
    return render(request, 'pknu_page.html', context=context)
def cs(request):
    crawl_data_cs = BlogData.objects.filter(tag="cs")
    context = {
        'crawl_data_cs':crawl_data_cs,
    }
    return render(request, 'cs_page.html', context=context)

def find(request):
    crawl_data_count = BlogData.objects.all().count()
    crawl_data_all = BlogData.objects.all()
    # crawl_list = serializers.serialize('json', crawl_data_all)

    if request.GET.get('search_instance'):
        form = request.GET.get('search_instance')
        crawl_search_data =BlogData.objects.filter(title__contains=form)
        context = {
            'crawl_search_data':crawl_search_data,
            'form': form
        }
        return render(request, 'find.html', context=context)
    else:
        return render(request, 'find.html')

def delete(request):
    BlogData.objects.all().delete()
    return redirect('/')
