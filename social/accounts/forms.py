from django.contrib.auth import get_user_model # returns the user thats currently active

from django.contrib.auth.forms import UserCreationForm # import that django's already build django creation forms.
'
class UserCreateForm(UserCreationForm):# inhert from the already built form, ensure they dont share the same name
# description:
# when the user comes in and ready to sign up, we call 'user creation form' form auth
# set up the mata class, which model attrubutes the user can set up.
    class Meta:
        fields = ('username', 'email', 'password1', 'password2') # fields we want to have user input

        model = get_user_model() # get the current model, whoever is using the website

    def __init__(self, *args, **kwargs):
        # EXTRA - if we want labels in the forms and templates you use this method
        # you create a type of dictorary/key value pairs
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name' # e.g if creating a twitter clone 'Display Name' would be 'Twitter handle'
        self.fields['email'].label = 'Email Address'
