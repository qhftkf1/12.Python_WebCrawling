from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.delete, name='delete'),
    path('find', views.find, name='find'),
    path('find/new', views.post_new, name ='find_new')
]
