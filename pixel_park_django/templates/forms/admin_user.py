from django.forms import ModelForm
from django import forms

from ...models import User


class UserForm(ModelForm):
    class Meta:
        model = User.User
        password = forms.CharField(
            label=False,
            max_length=100,
            widget=forms.PasswordInput(),
        )
        # Custom fields
        fields = ["name", "username", "email"]


    def clean(self):

        # data from the form is fetched using super function
        super(UserForm, self).clean()

        # extract the username and text field from the data
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        # conditions to be met for the username length
        if len(username) < 1:
            self._errors['username'] = self.error_class([
                'Field is required'])
        if len(email) < 1:
            self._errors['text'] = self.error_class([
                'Email is required'])

            # return any errors if found
        return self.cleaned_data
