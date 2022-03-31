from django.urls import path

from . import views


app_name = "postcrud_api"

urlpatterns = [
    path("posts", views.post_list, name="post_list"),
    path("posts/<int:pk>", views.post_detail, name="post_detail"),
    path("posts/<int:pk>/upvote", views.post_upvote, name="post_upvote"),
    path("posts/comments/create", views.create_comment, name="create_comment"),
    path("posts/<int:pk>/comments", views.comment_list, name="commment_list"),
    path("posts/comments/<int:pk>", views.comment_detail, name="commment_detail"),
]
