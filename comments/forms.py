from django import forms

class CommentForm(forms.Form):
  title = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'HtmlClassName', 'placeholder': 'HtmlPlaseholderName'}))
  body = forms.CharField(max_length=20, widget=forms.Textarea(attrs={'class': 'HtmlClassName', 'placeholder': 'HtmlPlaseholderName'}))
