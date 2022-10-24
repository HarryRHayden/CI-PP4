from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import UserEditView


# URL's for the page
urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),  # noqa
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),  # noqa
    path('edit_user', UserEditView.as_view(), name='edit_user'),
]
