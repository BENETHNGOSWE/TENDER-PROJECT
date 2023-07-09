from django import forms
from .models import TenderReg

class TenderRegForm(forms.ModelForm):
     class Meta:
          model =TenderReg 
          fields ='__all__'