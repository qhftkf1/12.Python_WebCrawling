from django.shortcuts import render
from django_crawl.models import BlogData

# Create your views here.
def index(request):
    crawl_data = BlogData.objects.all().count()

    context = {
        'num_data':crawl_data
    }

    return render(request, 'index.html', context=context)
