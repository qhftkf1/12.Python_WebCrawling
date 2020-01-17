from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('job',views.job,name='job'),
    path('link',views.link,name='link'),
    path('pknu',views.pknu,name='pknu'),
    path('cs',views.cs,name='cs'),
    path('delete', views.delete, name='delete'),
    path('find', views.find, name='find'),
    # path('find/post', views.post_new, name ='find_new')
]
