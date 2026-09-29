from django import forms
from django.contrib.auth import get_user_model
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