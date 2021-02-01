from django.db import models
from django.contrib import auth # django built in model for users

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):# inhert from the auth model

    def __str__(self):#string representation of the model
        return "@{}".format(self.username)
        # username is one of the attributes from the auth.models.User
