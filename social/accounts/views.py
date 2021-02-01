from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy # used incase someone is logged in or logged out
from django.views.generic import CreateView

from . import forms # connect to the from

# Create your views here.
class SignUp(CreateView):
    # the view where users can create new accounts
    form_class = froms.UserCreateForm # form connection
    success_url = reverse_lazy('login')
    # if successful transfer to the login page
    #template connection
    template_name = 'accounts/signup.html'
