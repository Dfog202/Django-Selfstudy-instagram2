from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='post', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    # like_users = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL,
    #     related_name='like_posts',
    #     through='PostLike',
    # )
    # tags = models.ManyToManyField('Tag', blank=True)

