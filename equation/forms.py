from django import forms


class EquationForm(forms.Form):
    parameter_a = forms.FloatField(label='a')
    parameter_b = forms.FloatField(label='b')
    parameter_c = forms.FloatField(label='c')