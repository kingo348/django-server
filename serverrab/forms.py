#forms.py
from django import forms

class CustomLoginForm(forms.Form):
    username = forms.CharField(label='Телефон клиента')
class WorkerLoginForm(forms.Form):
    username = forms.CharField(label='Почта')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

