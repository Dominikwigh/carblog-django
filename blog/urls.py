from django.urls import path
from .views import (Home, PostDetailView, AddPost, UpdatePost, DeletePost,
                    AddCategory, AddCategoryView, ContactView,
                    LikeView, AddComment)
from . import views

# Urls for all pages
urlpatterns = [
    # path('', views.home, name='home'),
    path('', Home.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('add_category/', AddCategory.as_view(), name='add_category'),
    path('post/edit/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('post/<int:pk>/delete', DeletePost.as_view(), name='delete_post'),
    path('category/<str:cat>/', AddCategoryView, name='category'),
    path('contact/', views.ContactView, name='contact'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('post/<int:pk>/comment/', AddComment.as_view(), name='add_comment'),
]
