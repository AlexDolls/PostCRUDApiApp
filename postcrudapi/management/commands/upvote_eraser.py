from django.core.management.base import BaseCommand
from postcrudapi.models import Post
from django.utils import timezone

import time
from threading import Thread

def upvote_eraser():
    while True:
        time.sleep(24*60*60)
        posts = Post.objects.all()
        for post in posts:
            post.upvotes = 0
            post.save()

class Command(BaseCommand):
    help = "Upvote eraser"

    def handle(self, *args, **options):
        background_thread = Thread(target = upvote_eraser)
        background_thread.start()
