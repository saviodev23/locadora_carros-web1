from django import forms
from django.forms import ModelForm
from locacao.models import Locacao


class FormAddLocacao(forms.Form):
    data_locacao = forms.DateField(label='Data de Locação')
    data_devolucao = forms.DateField(label='Data de Devolução')
    hora_locacao = forms.TimeField(label='Hora de Locação')
    hora_devolucao = forms.TimeField(label='Hora de Devolução')



class FormEditLocacao(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = ['status', 'data_locacao', 'hora_locacao', 'data_devolucao', 'hora_devolucao', 'automovel', 'valor_locacao', 'quilometragem']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'data_locacao': forms.DateInput(attrs={'class': 'form-control'}),
            'data_devolucao': forms.DateInput(attrs={'class': 'form-control'}),
            'hora_locacao': forms.TimeInput(attrs={'class': 'form-control'}),
            'hora_devolucao': forms.TimeInput(attrs={'class': 'form-control'}),
            'automovel': forms.Select(attrs={'class': 'form-control'}),
            'valor_locacao': forms.NumberInput(attrs={'class': 'form-control'}),
            'quilometragem': forms.NumberInput(attrs={'class': 'form-control'}),
        }