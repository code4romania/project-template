from django import forms


class SimpleForm(forms.Form):
    title = forms.CharField(label="Care este titlul documentului?")
    non_readable = forms.BooleanField(label="I can't read it", required=False)
    data = forms.DateField(label="Care este data la care a fost completat documentul?")
    tip_declaratie = forms.ChoiceField(label="Ce tip de declaratie de avere este completata?", choices=(("AVERE", "AVERE"), ("INTERESE", "INTERESE")))

