from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
from .models import Group, groupMember

from django.shortcuts import get_object_or_404
from django.contrib import messages
# Create your views here.

class CreateGroup(LoginRequiredMixin, generic.CreateView)
# The view that allows the user to create a forum.
    fields('name', 'description')
    # the fields from the model we want to the user to edit
    model = Group
    # DB connection with group DB/Model
    #NOTE STILL NEED TO CONNECT TO TEMPLATE

class SingleGroup(generic.DetailView):
# the view to see all the post in a group
    model = Group

class ListGroup(generic.ListView):
# the View that allows the user to see ALL the available form look into
    model = Group

class JoinGroup(LoginRequiredMixin, generic.RedirectView):
    #this is the view that enables the users to join the group
    # this will contain validation as you can not join a group twice.
    def get_redirect_url(self, *args, **kwargs):
        return reverse('group:single', kwargs={'slug':self.kwargs.get('slug')})
        #sends the users to the detail view of the group they want to join,
        # to know which group it is we get the slug pk on the current group being click
        # and match it with the same pk within the groups model.

    def get(self, request, *args, **kwargs):
        # try to get a group this person is looking at or return a 404 page
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))
        try:
            GroupMemer.objects.create(user=self.request.user, group=group)
            # try to get a group member object where the user is equal to the current user and the group is equalto group
        except IntegrityError:
            messages.warning(self.request,('WARNING! Already a member'))
        else:
            messages.success(self.request,'You are now a member')
        return super().get(request, *args, **kwargs)

class LeaveGroup(LoginRequiredMixin, generic.RedirectView):
# description: this view enables the user to leave a group if they are currently
# in one. once a person leave a leavegroup funtion view send the user back to the
# detail view of group they just left. also there is a get function that...
# if they try to leave the group it check that user are a meber of selected the group
# and if sends an error to the user that -they are not in the group they are leaving.
# else, if they are in the member list of the group you can delete them and send a success
# message.
    pass
    def get_redirect_url(self, *args, **kwargs):
    #the leave group view is exactly the same with JoinGroup View, where if the
    # user leves the group it send them to the froup detail page
        return reverse('group:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        # the validation method that prevents the user from leaving a group if
        # they're not already in the current one they want to leave
        try:
        # try to create a membership object that gets the model infromation
        # from the GroupMember model, more specifically(filter) the current user
        # current group slug. tooo
            membership = models.GroupMember.objects.filter(
            user=self.request.user,
            group__slug=self.kwargs.get('slug')
            )
        except models.GroupMember.DoesNotExist:
            # if the member is not a member of the group
            messages.warning(self.request,'Sorry you are not in this group!')
        else:
            membership.delete()
            messages.success(self.request, 'You have successfully left the group!')
        return super().get(request, *args, **kwargs)
