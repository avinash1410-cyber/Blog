from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)


    def our_email(self,*args,**kwargs):
        email=self.cleaned_data('email')
        print(email)
        if email.endswith(".edu"):
            raise forms.ValidationError("Enter Valid Id")
        return email