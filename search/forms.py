from __future__ import absolute_import

from django import forms

class SearchForm(forms.Form):
    title = forms.CharField(max_length=100)
