from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class PostCRUD(object):
    @classmethod
    def create_post(cls, post_data: dict):
        serializer = PostSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
            data_copy = serializer.data.copy()
            data_copy["link"] = f"/posts/{data_copy['pk']}"
            post = Post.objects.get(pk=data_copy["pk"])
            post.link = data_copy["link"]
            post.save()
            return {"detail": data_copy, "status": status.HTTP_201_CREATED}
        return {"detail": serializer.errors, "status": status.HTTP_400_BAD_REQUEST}

    @classmethod
    def get_post(cls, post: Post):
        serializer = PostSerializer(post)
        return serializer.data

    @classmethod
    def get_post_list(cls):
        posts = Post.objects.all()
        serializer_for_posts = PostSerializer(instance=posts, many=True)
        return serializer_for_posts.data

    @classmethod
    def update_post(cls, post_data: dict, post: Post):
        serializer = PostSerializer(post, data=post_data)
        if serializer.is_valid():
            serializer.save()
            return {"detail": serializer.data, "status": status.HTTP_200_OK}
        return {"detail": serializer.errors, "status": status.HTTP_400_BAD_REQUEST}

    @classmethod
    def upvote_post(cls, post: Post):
        post_data = cls.get_post(post)
        post_data["upvotes"] = post.upvotes + 1
        if serializer.is_valid():
            serializer.save()
            return {"detail": serializer.data, "status": status.HTTP_200_OK}
        return {"detail": serializer.errors, "status": status.HTTP_400_BAD_REQUEST}


class CommentCRUD(object):
    """
    Comment model administrative functions
    """

    @classmethod
    def create_comment(cls, comment_data: dict):
        serializer = CommentSerializer(data=comment_data)
        if serializer.is_valid():
            serializer.save()
            return {"detail": serializer.data, "status": status.HTTP_201_CREATED}
        return {"detail": serializer.errors, "status": status.HTTP_400_BAD_REQUEST}

    @classmethod
    def get_comment(cls, comment: Comment):
        serializer = CommentSerializer(comment)
        return serializer.data

    @classmethod
    def get_comment_list(cls, post: Post):
        post_comments = post.comment_set.all()
        serializer_for_comments = CommentSerializer(instance=post_comments, many=True)
        return serializer_for_comments.data

    @classmethod
    def update_comment(cls, comment_data: dict, comment: Comment):
        serializer = CommentSerializer(comment, data=comment_data)
        if serializer.is_valid():
            serializer.save()
            return {"detail": serializer.data, "status": status.HTTP_200_OK}
        return {"detail": serializer.errors, "status": status.HTTP_400_BAD_REQUEST}


"""
Post CRUD API Views
"""


@api_view(["GET", "POST"])
def post_list(request):
    if request.method == "GET":
        return Response(PostCRUD.get_post_list())

    elif request.method == "POST":
        post = PostCRUD.create_post(request.data)
        return Response(post["detail"], post["status"])


@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, pk):
    """
    Retrieve, update or delete a customer by id/pk.
    """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(PostCRUD.get_post(post=post))

    if request.method == "PUT":
        update_post = PostCRUD.update_post(post_data=request.data, post=post)
        return Response(update_post["detail"], update_post["status"])

    if request.method == "DELETE":
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["PUT"])
def post_upvote(request, pk):
    """
    Upvote endpoint
    """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    upvote_post = PostCRUD.upvote_post(post=post)
    return Response(upvote_post["detail"], upvote_post["status"])


"""
Comment CRUD API Views
"""


@api_view(["POST"])
def create_comment(request):
    comment = CommentCRUD.create_comment(comment_data=request.data)
    return Response(comment["detail"], comment["status"])


@api_view(["GET"])
def comment_list(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(CommentCRUD.get_comment_list(post=post))


@api_view(["GET", "PUT", "DELETE"])
def comment_detail(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(CommentCRUD.get_comment(comment=comment))

    if request.method == "PUT":
        update_comment = CommentCRUD.update_comment(
            comment_data=request.data, comment=comment
        )
        return Response(update_comment["detail"], update_comment["status"])

    if request.method == "DELETE":
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
