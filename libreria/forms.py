from dataclasses import field

from django import forms
from pyexpat import model

from .models import paciente


class pacienteForm(forms.ModelForm):
    class Meta:
        model = paciente
        fields = '__all__'