from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(
        label=False,
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Username or Email'})
    )
    password = forms.CharField(
        label=False,
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Password'}),
    )
