from django import forms
from django.core import validators

class SuggestionForm(forms.Form):
    suggestion = forms.CharField(
        validators=[validators.validate_slug],
        label='Suggestion',
        max_length=240
        )
