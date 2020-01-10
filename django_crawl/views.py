from django.shortcuts import render
from django_crawl.models import BlogData
from django.shortcuts import redirect

# Create your views here.
def index(request):
    crawl_data_count = BlogData.objects.all().count()
    crawl_data_all = BlogData.objects.all()
    context = {
        'crawl_data_count':crawl_data_count,
        'crawl_data_all':crawl_data_all,
    }

    return render(request, 'index.html', context=context)

def delete(request):
    BlogData.objects.all().delete()
    return redirect('/')
