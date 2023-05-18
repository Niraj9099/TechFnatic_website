from django.shortcuts import render
from .models import WebSiteData, CardData
from .form import Contact_Form
from django.contrib import messages
# Create your views here.

def Home(request):
    data = WebSiteData.objects.get(id=1)
    card = CardData.objects.all()
    return render(request, 'home.html', {'data':data, 'card':card})

def card(request, pk):
    data = WebSiteData.objects.get(id=1)
    card = CardData.objects.get(id=pk)
    return render(request, 'card.html', {'data':data, 'card':card})

def contactForm(request):
    data = WebSiteData.objects.get(id=1)
    if request.method == 'POST':
        fm = Contact_Form(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['first_name']
            fm.save()
            messages.success(request, f'Hello {name}, Message was Successfully send !!!')
            fm = Contact_Form()
    else:
        fm = Contact_Form()
    return render(request, 'contact.html', {'form':fm,'data':data})


def privatePolicy(request):
    data = WebSiteData.objects.get(id=1)
    return render(request, 'policy.html',{'data':data})


def terms_condition(request):
    data = WebSiteData.objects.get(id=1)
    return render(request, 'terms_condition.html',{'data':data})