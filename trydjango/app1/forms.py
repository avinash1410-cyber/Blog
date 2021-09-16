from django import forms
from .models import BPost

class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)

class BPMform(forms.ModelForm):
    class Meta:
        model=BPost
        fields=['title','content','slug']



        def clean_title(self,*args,**kwargs):
            instance=self.instance
            title=self.cleaned_data.get('title')
            qs=BPost.objects.filter(title__iexact=title)
            if instance is not None:
                qs=qs.exclude(pk=instance.pk)
            if qs.exists():
                raise forms.ValidationError("Title Already Used")
            return title