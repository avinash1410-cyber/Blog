from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
# Dont Repeat Yourself = DRY
from .forms import ContactForm


def Home(request):
    my_title = "Hello there...."
    context = {"title": "my title"}
    if request.user.is_authenticated:
        context = {"title": my_title, "My_List": [1, 2, 3, 4, 5]}
    return render(request, "home.html", context)



def Contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact us",
        "form": form
    }
    return render(request, "Contact.html", context)


def About(request):
    return render(request,'About.html',{"Query":"Our Company Is A Kind Of StarUp Start By License By GOI In Year 2009 And It IS A One Of The Fatest Growing Cyber Security Providre Compnay In The World"})
