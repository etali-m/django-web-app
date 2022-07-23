
from django import forms

from listings.models import Band, Listing

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False) #permet de définir un champ name 
    email = forms.EmailField()              #... email
    message = forms.CharField(max_length=1000) #... message


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        #fields = '__all__'    this line is to add all the fields of the class in the form
        exclude = ('active', 'official_homepage') #this line is for excluding this two field in the form



class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'