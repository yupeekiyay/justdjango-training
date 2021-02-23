from django import forms
from django.db.models import fields
from .models import Lead

class LeadModelForm(forms.ModelForm):
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # age=forms.IntegerField(min_value=0)
    class Meta:
        model = Lead
        fields=('first_name','last_name','age','agent')