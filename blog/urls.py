from . import views
from django.contrib.auth import views as auth_views
from django.urls import path


# URL's for the page
urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),  # noqa
]
