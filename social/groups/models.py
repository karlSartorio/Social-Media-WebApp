from django.db import models

#GROUPS/MODELS.PY file

from django.utils.text import slugify
 # package - slugify, it allows to remove any characters that arent alpha numeric.
 # use case - if user input a string with white spaces, this import allows the user
 #            to work with this string by convering the white space into dashes.

 import misaka
 # https://misaka.61924.nl/
 # allows the use of markdown inside of the post.

from django.contrib.auth import get_user_model
User = get_user_model()
# get the the model of active user then be using their model information latet


from django import template
register = template.Library()
#this will be used later on the development
# will need to create other functionality to fully describe

# Create your models here#
class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    #name of the group, only allowing it to be unique no overlapping names
    slug = models.SlugField(allow_unicode=True, unique=True)
    #the slug field, must be unique so that group name and slugs dont overlap each other
    description = models.TextField(blank=True, default='')
    # group description attribute, description of group must not be blank
    description_html = models.TextField(editable=False, default='', blank='True')
    #description_html - if we want the html version of the description, also cant be black
    # could be used later.
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        #save method, before saving there are some formatting that needs to
        # to be processed to be saved properly

        self.slug = slugify(self.name)
        # this is where slugify come into play, replaces values to be able to be saved
        self.description_html = misaka.html(self.description)
        # this is where misaka comes into play, allows markdown in the description
        super().save(*arg, **kwargs)


        def get_absolute_url(self):
            return reversed('groups:single', kwargs={'slug':self.slug})

        class Meta:
            ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)
    # the member is related to the group class through the ForeignKey
    # whoich we called memberships

    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)
    #This takes the user that was stated earlier to the script, the current active
    # use. then we get that user and link them to the various groups they belong to and/or
    # have them a member of.

    def __str__(self):
        # return username attribute instead of a whole object
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')
