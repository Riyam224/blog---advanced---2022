from telnetlib import NAMS
from django.urls import path
from . import views 



urlpatterns = [


    path('about/', views.about, name="blog-about"),

    path('', views.PostListView.as_view(), name="blog-home"),
    path('post-new/', views.PostCreateView.as_view(), name="blog-new"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="blog-detail"),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name="blog-update"),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name="blog-delete")
]
