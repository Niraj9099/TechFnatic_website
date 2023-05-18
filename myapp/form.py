from django import forms
from .models import ContectForm

class Contact_Form(forms.ModelForm):
    class Meta:
        model = ContectForm
        fields = '__all__'
        widgets = {'first_name':forms.TextInput(attrs={'class':'name form-control'}),
                    'last_name':forms.TextInput(attrs={'class':'name form-control'}),
                   'email':forms.EmailInput(attrs={'class':'email form-control'}),
                   'phone_number':forms.NumberInput(attrs={'class':'email form-control'}),
                   'select_product':forms.Select(attrs={'class':'email form-control'}),
                   'message':forms.Textarea(attrs={'class':'message form-control'}),
                   }
        