from django import forms
#from bigdata.views import get_my_choices
#from .views import page1
#from bigdata.functions import get_my_choices
#import .views
#from .models import Join

def get_my_choices():
	import subprocess
	string="hdfs dfs -ls /"
	l=[]	
	j=1
	s=subprocess.Popen(string,stdout=subprocess.PIPE,shell=True)
	#string1="ls"
	#s1=subprocess.Popen(string1,stdout=subprocess.PIPE,shell=True)
	#print "lololololol  %s" %(s1.communicate()[0])
	st=s.communicate()[0].split('\n')[1:]
	st=st[:len(st)-1]
	print "Bhoot"
	for i in st:
		#print i.split(' ')	
		temp=i.split(' ')
		z= temp[len(temp) -1]
		#print type(temp)	
		l.append((j,z))
		j=j+1
	return l

class DropDlist(forms.Form):
	#filename=forms.CharField(required=True)
	#progname=forms.CharField(required=True)
	#outputfold=forms.CharField(required=True)
	Select_File = forms.ChoiceField(choices=get_my_choices())
	def __init__(self, *args, **kwargs):
        	super(DropDlist, self).__init__(*args, **kwargs)
        	self.fields['Select_File'] = forms.ChoiceField(
           	   choices=get_my_choices() )


class uploadfile(forms.Form):

	#docfile = forms.FileField(label='Select a file', help_text='max. 42 megabytes')
	Upload_your_File = forms.CharField(required=True)
	


class mapred(forms.Form):
	mapper = forms.FileField(label='Select a file', help_text='select mapper file')
	reducer = forms.FileField(label='Select a file', help_text='select reducer file')
	Output_Folder_Name=forms.CharField(required=True)
	
class mapred1(forms.Form):
	CHOICES = (
        ('1', 'wordcount'),
        ('2', 'Mean'),
	)
	Select_Pre_Built_Program = forms.ChoiceField(choices=CHOICES)
	Output_Folder_Name=forms.CharField(required=True)


class sparkmapred(forms.Form):
	mapper = forms.FileField(label='Select a file',help_text='select a spark mapreduce file')
	
	output=forms.CharField(required=True)


	
  
