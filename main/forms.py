from django import forms

from main.models import CommentModel


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput())
    class Meta:
        model = CommentModel
        fields = ('user', 'text',)

