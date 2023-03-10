"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from magnolia_tree import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', views.home_page, name='home'),
    path('classes/', views.classes_page, name='classes'),
    path('contact/', views.contact_page, name='contact'),
    path('blog/', views.BlogPage.as_view(), name='blog'),
    path('<slug:slug>/', views.BlogPostDetail.as_view(), name='blog_post'),
    path('like/<slug:slug>', views.LikeBlogPost.as_view(), name='like_post'),
    path(
        'update-comment/<int:pk>',
        views.UpdateComment.as_view(),
        name='update_comment'
        ),
    path(
        'delete_comment/<slug:slug>/<int:pk>/',
        views.DeleteComment.as_view(),
        name='delete_comment'
        ),
    path(
        'blog/create_post',
        views.UserBlogPost.as_view(),
        name='create_post'
        ),
    path('accounts/', include('allauth.urls')),
]
