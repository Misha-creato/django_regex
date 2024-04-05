from django import forms


class RegexForm(forms.Form):
    pattern = forms.CharField()
    string = forms.CharField()
