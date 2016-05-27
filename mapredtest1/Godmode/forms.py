from django import forms
#from bigdata.views import get_my_choices
#from .views import page1
#from bigdata.functions import get_my_choices
#import .views
#from .models import Join
'''
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
'''

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


class premlform(forms.Form):
	CR=forms.DecimalField(label='Crime Rate',decimal_places=6)
	ZN=forms.DecimalField(label='Land Zoned over float5K sq.ft ',decimal_places=6)
	INDUS=forms.DecimalField(label='Proportion of Non retail business acres per town',decimal_places=6)
	CHAS=forms.DecimalField(label='Input 1 if Tracts Bound River Otherwise input 0',decimal_places=6)
	NOX=forms.DecimalField(label='Nitrous Oxide Concentration in Parts per 10 million',decimal_places=6)
	RM=forms.DecimalField(label='Number of Rooms per Dwelling',decimal_places=6)
	AGE=forms.DecimalField(label='Proportion of Owner occupied Units built prior to 1940',decimal_places=6)
	DIS=forms.DecimalField(label='weighted distances to five Boston employment centre',decimal_places=6)

	RAD=forms.DecimalField(label='index of accessibility to radial highways',decimal_places=6)
	TAX=forms.DecimalField(label='full-value property-tax rate per $10,000',decimal_places=6)
	PTRATIO=forms.DecimalField(label='pupil-teacher ratio by town',decimal_places=6)
	B=forms.DecimalField(label='1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town',decimal_places=6)


	LSTAT=forms.DecimalField(label='% lower status of the population',decimal_places=6)
	#MEDV=forms.DecimalField(label='Median value of owner-occupied homes in $1000',decimal_places=6)


class customform1(forms.Form):
	CHOICES = (
        ('1', 'Comma (,)'),
        ('2', 'Dot (.)'),
	('3', 'Colon (:)'),
	)
	delim= forms.ChoiceField(label="Select your Deliminator", choices=CHOICES)
	dataset = forms.FileField(label='Upload Your Dataset')

class customform2(forms.Form):
	CHOICES = (
        ('1', 'Linear Regression With SGD'),
        ('2', 'Algo 2'),
	)
	algo= forms.ChoiceField(label="Select your Machine Learning Algorithm", choices=CHOICES)
	labelcolumn = forms.CharField(label='Enter column number of the label')

class customform3(forms.Form):
	stepsize=forms.CharField(label="Enter Step Size",required=True)
	iterations=forms.CharField(label="Enter number of Iterations",required=True)
	modelname=forms.CharField(label="Enter name of the model",required=True)
	

class customform4(forms.Form):
	spacefeatures=forms.CharField(label="Enter features in space separated manner",required=True)	
	







	
  
