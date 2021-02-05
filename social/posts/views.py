from django.shortcuts import render
#POST VIEWS.PY
# Create your views here.

# ensure people has to be logged into do some views required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
# used when a user want to delete some post

from django.views import generic

from django.http import Http404
#used for error message

from braces.views import SelectRelatedMixin
# A simple mixin which allows you to specify a list or tuple of foreign
#  key fields to perform a select_related on. - will be display later on

from. import models

from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()
# when someone is logged in a session i can get this User oject and call
# off the current users attributes.


class PostListClass(SelectRelatedMixin, generic.ListView):
#Description:
    # once you select a person you can see the user's post or select a
    # group see the posted post.
    model = models.Post
    select_related = ('user' 'group')
    #selectedRelatedMixin method /attribute that allows us to create a tuple
    # of related models which are foreign keys to the post

class UserPost(generic.ListView):
    model = models.Post
    template_name = 'post/user_post_list.html'

    def get_queryset(self):
        #creating a method of  grabbed item in the list.
        # the first method is going to 'try' to set the post.user/user that belongs
        # to a particular post equal to The current users related post and then
        # get where the username is ecaxtly whatever the user that currently logged in
        # or whatever user it happens to click on. if the user does not exisit raise an error
        # else then return all the post.
        try:
            self.post.user = User.object.prefetch_related('posts').get(username__iexac=self.kwargs.get('usernanme'))
        except user.DoesNotExist:
            raise Http404
        else:
            return self.post_user.post.all()


    def get_context_data(self, **kwargs):
        #dexcription: method of returning the context data object esential connected
        #             to the whoever posted that specific user
        context = super().get_context_data(**kwargs)
        context = ['post_user'] = self.post_user
        return context

class PostDetail(selectedRelatedMixin, generic.DetailView):
    # description: the detail view when you click on a singular post
    models = models.post
    select_related = ('user', 'group')

    def get_queryset(self):
        # get the queryset for the post and filter it by the extaxt username
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwarg.get('username'))

class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
# the view that allows the users to create post
    fields = ('message', 'group')
    #the fields we want the users to edit
    model = models.Post

    def form_valid(self, form):
        #to ensure that there is no diplicate when saving the models
        # connect the post.user with the actual user
        self.object = form.save(commit=false)
        self.object.user = self.request.user
        self.obeject.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, SelectedRelatedMixin, generic.DeleteView):
    # the view that deletes post
    model = models.Post
    select_related = ('user', 'group')

    success_url = reverse_lazy('posts:all')
    # redirect users to another once the deletion of a post is done
    # which is the list of all the post
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Post Delete')
        return super().delete(*argsm **kwargs)
