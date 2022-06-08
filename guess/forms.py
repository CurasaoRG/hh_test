from django import forms


class GuessForm(forms.Form):
    parameter_n = forms.IntegerField(label='n')