from django.forms import ModelForm


from django import forms
from meseros.models import Meseros




class MeserosForm(ModelForm):
    class Meta:
        model = Meseros
        fields = ('nombre', 'edad', 'pais')



# class MeserosForm(forms.Form):
#     nombre = forms.CharField(max_length=40)
#     edad = forms.IntegerField(max_value=100)
#     pais = forms.CharField(max_length=40)
