from django.forms import ModelForm


from django import forms
from platos.models import Platos




class PlatosForm(ModelForm):
    class Meta:
        model = Platos
        fields = ('nombre', 'precio', 'pais')



# class MeserosForm(forms.Form):
#     nombre = forms.CharField(max_length=40)
#     edad = forms.IntegerField(max_value=100)
#     pais = forms.CharField(max_length=40)
