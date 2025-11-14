from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Post is a model
class Post(models.Model):
    title = models.CharField(max_length=100)  # is a character field
    content = models.TextField()
    # date_posted = models.DateTimeField(auto_now_add=True) can't change post time
    date_posted = models.DateTimeField(default=timezone.now)
    # One-to-many relation: 1 user can make multiple posts
    # but a post can have only 1 author
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # If a user is deleted, all their posts will be deleted

    # show title when in a query result
    def __str__(self):
        return self.title
