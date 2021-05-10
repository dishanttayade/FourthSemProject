from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

USER_CHOICES = [
    ('D', 'Doctor'),
    ('P', 'Patient')
]

class UserCreateForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=USER_CHOICES, required=True)
    class Meta:
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", "user_type")
        model = get_user_model()
        #exclude = ('username.help_text')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields["username"].label = "Username"
        #self.fields["email"].label = "Email address"
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            

