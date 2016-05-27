from django import forms

#from .models import Join

class EmailForm(forms.Form):
	filename=forms.CharField(required=True)
	progname=forms.CharField(required=True)
	outputfold=forms.CharField(required=True)


  
