from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('post/<str:pk>', views.post, name='post.html')
]
