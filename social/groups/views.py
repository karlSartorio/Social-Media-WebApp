from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
from .models import Group, groupMember
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
