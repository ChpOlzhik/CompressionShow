from django import forms


class TextForm(forms.Form):
    txt = forms.Textarea()
