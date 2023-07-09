from django import forms
from .models import BidderReg,bidapplication

class Regform(forms.ModelForm):
    class Meta:
        model = BidderReg
        fields = '__all__'



class applicationform(forms.ModelForm):
    class Meta:
        model = bidapplication
        fields = '__all__'        