from django.db import models
#POST/MODELS.PY
from django.urls import reverse
# method to redirect to another page

from django.conf import settings
# allows custom settings.

import misaka
# allow markdown on post

from groups.model import Group
# to make a link a post to a group
# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts')
    # link the made post with the auther of the post user model
    created_at = models.DateTimeField(auto_now=True)
    # save the current time its created
    message = models.TextField()
    # messate attribute, the context of the post
    message_html = models.TextField(editable=False)
    # allow markdown on message attribute,
    # users cant directly edit it but grab it directly from message which will be done
    # in the saved function of the model
    group = models.ForeignKey(Group, related_name='posts', null=True, Blank = True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwars):
        self.message_html = misaka.html(self.message)
        # this is where the markdown of the message happens
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # redirect the user to a template, with the kwargs that will inject the
        # users username, and pk(primary key) a method to relate post to url
        return reverse('posts:single', kwargs={'username':self.user.username,
                                        'pk': self.pk})

    def Meta:
        ordering = ['-created_at'] # DESC post on top
        unique_together = ['user', 'message'] # every message is uniquely linked to a user. 
