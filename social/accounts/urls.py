from django.urls import path
from django.contrib.auth import views as auth_views
#django already contains a login view and logout view we simply import and use it
from . import views


app_name ='accounts'# this will be the reference text for relative URL

urlpatterns =[
path('login/',
    auth_views.LoginView.as_view(template_name='accounts/login.html'),
    name='login'),
path('logout/',
     auth_views.LogoutView.as_view(),
     name='logout'),
# The two method are how to set up the url mapping for the django onboard
# login and logout views. we simply call the imported view, set it as_view(),
# within the parameter we give the template name(direct which tempalate it will
# be). the logout view doesnt need a tempalate as its going to redirect the user
# to the index/home page

path('signup/',
     views.SignUp.as_view(), name='signup'),

]
