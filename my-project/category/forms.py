from django import forms

class AddCategory(forms.Form):
    name = forms.CharField(max_length=10)