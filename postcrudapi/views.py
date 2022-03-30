from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Comment

# Create your views here.

class PostCRUD(object):
    @classmethod
    def create_post(cls, title: str, link: str, author_name: str):
        pass

    @classmethod
    def get_post(cls, post_id: int):
        pass

    @classmethod
    def get_post_list(cls):
        pass

    @classmethod
    def update_post(cls, post_data: dict):
        pass

    @classmethod
    def delete_post(cls, post_id: int):
        pass


class CommentCrud(object):
    @classmethod
    def create_comment(cls, author_name: str, content: str, post: Post)
        pass

    @classmethod
    def get_comment(cls, comment_id: int):
        pass

    @classmethod
    def get_comment_list(cls, post: Post):
        pass

    @classmethod
    def update_comment(cls, comment_data: dict):
        pass

    @classmethod
    def delete_comment(cls, comment_id: int):
        pass


def index(request):
    return HttpResponse("It's index view!")
