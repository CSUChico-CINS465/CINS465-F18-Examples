from django import forms

class SuggestionForm(forms.Form):
    suggestion = forms.CharField(
        label='Suggestion',
        max_length=240
        )
