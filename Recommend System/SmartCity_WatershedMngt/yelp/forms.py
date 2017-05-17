from django import forms
from yelp.models import *

class NameForm(forms.Form):
    your_name = forms.ChoiceField(choices=(rec.objects.values_list('uID','uID')), label='User ID')