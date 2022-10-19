from . import views
from django.contrib.auth import views as auth_views
from django.urls import path



# URL's for the page

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
]