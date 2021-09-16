from django import forms

class BPform(forms.Form):
    title=forms.CharField()
    content=forms.CharField(widget=forms.Textarea )
    slug=forms.CharField()