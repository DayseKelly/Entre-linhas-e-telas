from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html
from .models import Usuario

User = get_user_model()

class UsuarioForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label='Nome de usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput, strip=False)

    class Meta:
        model = Usuario
        fields = ['data_nasc', 'rg', 'cpf', 'escola']
        labels = {
            'data_nasc': 'Data de nascimento',
            'rg': 'RG',
            'cpf': 'CPF',
            'escola': 'Escola',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['username'].initial = self.instance.user.username
            self.fields.pop('password')
        else:
            self.fields['password'].required = True

    def clean_username(self):
        username = self.cleaned_data['username']
        users = User.objects.filter(username=username)
        if self.instance.pk:
            users = users.exclude(pk=self.instance.user_id)
        if users.exists():
            raise forms.ValidationError('Este nome de usuário já está em uso.')
        return username


class CadastroPublicoForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label='Nome de usuário')
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=password_validators_help_text_html(),
    )
    password_confirmation = forms.CharField(
        label='Confirme a senha',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta:
        model = Usuario
        fields = ['data_nasc', 'rg', 'cpf', 'escola']
        labels = {
            'data_nasc': 'Data de nascimento',
            'rg': 'RG',
            'cpf': 'CPF',
            'escola': 'Escola',
        }
        widgets = {'data_nasc': forms.DateInput(attrs={'type': 'date'})}

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nome de usuário já está em uso.')
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmation = cleaned_data.get('password_confirmation')

        if password and confirmation and password != confirmation:
            self.add_error('password_confirmation', 'As senhas não coincidem.')
        elif password:
            user = User(username=cleaned_data.get('username', ''))
            try:
                validate_password(password, user)
            except ValidationError as error:
                self.add_error('password', error)

        return cleaned_data

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        perfil = super().save(commit=False)
        perfil.user = user
        perfil.save()
        return perfil