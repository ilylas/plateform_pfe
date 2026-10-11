from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(
        label='Je suis',
        choices=[
            (User.Role.ETUDIANT, 'Étudiant'),
            (User.Role.ENCADRANT_PRO, 'Encadrant professionnel'),
        ],
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'role', 'entreprise')