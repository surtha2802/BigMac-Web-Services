from django.shortcuts import render
from .forms import premlform,customform1,customform2,customform3,customform4
from django.template import Context
from django.template.loader import get_template

from django.http import HttpResponse,HttpResponseRedirect
import os,subprocess


def MLHome(request):
	template="home.html"
	if request.method=='POST':
		print 'form1 yyyyy'	
		
		if 'form11' in request.POST:
			print 'formml 1111'	
			return HttpResponseRedirect('/mlpage1/')
		elif 'form22' in request.POST:
			print 'formml 2222'
			return HttpResponseRedirect('/mlpage4/')

	return render(request,template)


def index(request):
	template="index.html"
	return render(request,template)


def mlpage1(request):
	template="mlpage1.html"
	return render(request,template)


def mlpage2(request):
	temp=0
	form=premlform(request.POST)
	if request.method=='POST':
		if form.is_valid():
				CR=float(form.cleaned_data['CR'])
				ZN=float(form.cleaned_data['ZN'])
				INDUS=float(form.cleaned_data['INDUS'])
				CHAS=float(form.cleaned_data['CHAS'])
				NOX=float(form.cleaned_data['NOX'])
				RM=float(form.cleaned_data['RM'])
				AGE=float(form.cleaned_data['AGE'])
				DIS=float(form.cleaned_data['DIS'])
				RAD=float(form.cleaned_data['RAD'])
				TAX=float(form.cleaned_data['TAX'])
				PTRATIO=float(form.cleaned_data['PTRATIO'])
				B=float(form.cleaned_data['B'])
				LSTAT=float(form.cleaned_data['LSTAT'])
				

				import numpy as np
				import pandas as pd
				import scipy.stats as stats
				import matplotlib.pyplot as plt
				import sklearn
				from sklearn.externals import joblib
				import pickle
				from sklearn.datasets import load_boston
				boston=load_boston()
				bos=pd.DataFrame(boston.data)



				from sklearn.linear_model import LinearRegression
				hp = joblib.load('/root/Documents/filename.pkl') 
				j=[(1,CR) ,(1,ZN) ,  (1,INDUS), (1,CHAS),  (1,NOX),  (1,RM),  (1,AGE), (1,DIS), (1,RAD), (1,TAX), (1,PTRATIO), (1,B),(1,LSTAT)]
				bos1=pd.DataFrame(j)
				#hp=pickle.loads(houseprice)
				print boston.target[:5]
				print type(bos1),"weopwiporiopoepwrwwhfjhfdskhjfkdhsfj"
				print bos.head(1),"mlmlsamlmsalsmdlksdladjgDJGJgshasd"
				print bos1.T,"opopopopopopopo"

				temp=hp.predict(bos1.T.head(1))	
				print temp
				command="echo %s > /root/Desktop/resultHPrice.LOL" % temp
				os.system(command)
				return HttpResponseRedirect('/mlpage3/')
				
	template="mlpage2.html"
	return render(request,template,{'answer':temp,'form':form})

def mlpage3(request):
	f=open("/root/Desktop/resultHPrice.LOL","r")
	temp=f.read()
	temp=temp[1:len(temp)-2]
	
	print temp
	print "LOLOLOLO",temp
	template="mlpage3.html"
	return render(request,template,{'run':temp})



def mlpage4(request):
	template="mlpage4.html"
	
	return render(request,template)


def mlpage5(request):
	template="mlpage5.html"
	form=customform1(request.POST,request.FILES)
	print request.POST
	if request.method=='POST':
		print "mmmmm"
		
		print "nnnnnn"
		#delim=str(form.cleaned_data['delim'])
		dataset=str(request.POST.get('dataset',''))
		delim=str(request.POST.get('delim',''))
		command1="rm -rf /root/Desktop/delim.LOL;echo %s >> /root/Desktop/delim.LOL ; echo %s >> /root/Desktop/delim.LOL" % (delim,dataset)
		os.system(command1)

		command="hdfs dfs -put	/root/Desktop/%s /" %dataset
		os.system(command)
		return HttpResponseRedirect('/mlpage6/')
			
	return render(request,template,{'form':form})


def mlpage6(request):
	template="mlpage6.html"
	form=customform2(request.POST)
	if request.method=='POST':
		if form.is_valid():
			
			algo=str(form.cleaned_data['algo'])
			
			labelcolumn=str(form.cleaned_data['labelcolumn'])

			command1="rm -rf /root/Desktop/label.LOL;echo %s >> /root/Desktop/label.LOL" % (labelcolumn)
			os.system(command1)

			if str(algo)=="1":
					
				return HttpResponseRedirect('/SGD/')
			else:
				return HttpResponseRedirect('/UnderCons/')				
			
			
			
					
			
	return render(request,template,{'form':form})


def SGD(request):
	template="SGD.html"
	form=customform3(request.POST)
	if request.method=='POST':
		if form.is_valid():
			stepsize=str(form.cleaned_data['stepsize'])			
			iterations=str(form.cleaned_data['iterations'])
			modelname=str(form.cleaned_data['modelname'])
			command1="rm -rf /root/Desktop/parameters.LOL;echo %s >> /root/Desktop/parameters.LOL;echo %s >> /root/Desktop/parameters.LOL;echo %s >> /root/Desktop/parameters.LOL" % (stepsize,iterations,modelname)
			os.system(command1)

			comm="spark-submit /root/Desktop/mpv2/mapredtest1/Godmode/MLModels/linearSGD.py"
			os.system(comm)
			return HttpResponseRedirect('/modelresult/')		
	return render(request,template,{'form':form})

def modelresult(request):

	template="modelresult.html"
	return render(request,template)

def valpred(request):
	template="valpred.html"
	return render(request,template)

def satisfied(request):
	template="satisfied.html"
	form=customform4(request.POST)
	if request.method=='POST':
		if form.is_valid():
			features=str(form.cleaned_data['spacefeatures'])
			strin="echo %s > /root/Desktop/features.LOL" % features
			strin2="pyspark /root/Desktop/mapredtest1/Godmode/MLModels/modelrun.py"
			os.system(strin)
			os.system(strin2)
			return HttpResponseRedirect('/show1')
	return render(request,template,{'form':form})

	

def show1(request):
	template="show1.html"
	f=open("/root/Desktop/predicted.txt","r")
	run=f.read().strip()
	return render(request,template,{'run':run})
	
def notsatisfied(request):
	param=open("/root/Desktop/parameters.LOL","r")
	temp=param.readlines()
	supermodel=temp[2].strip()
	st="rm -rf %s" %supermodel
	os.system(st)
	return HttpResponseRedirect('/mlpage6/')

def modelsave(request):
	param=open("/root/Desktop/parameters.LOL","r")
	temp=param.readlines()
	supermodel=temp[2].strip()
	command1="tar -zcvf %s.tar.gz %s" % (supermodel,supermodel)
	os.system(command1)
	comm="hdfs dfs -copyFromLocal %s.tar.gz /" %(supermodel)
	os.system(comm)
	command="echo %s >> /root/Desktop/modelsaves.LOL" % supermodel
	os.system(command)
	command2=r"python /root/Desktop/mpv2/mapredtest1/Godmode/MLModels/downmodel.py"
	os.system(command2)
	
	
	return HttpResponseRedirect('/modelsaved/')

def modelsaved(request):
	template="modelsaved.html"
	return render(request,template)

def downmodel(request):
	template="modelsav.html"
	return render(request,template)

def modeldown(request):
	template="downmodel.html"
	return render(request,template)
	

def plotgraph(request):
	template="graph.html"
	param=open("/root/Desktop/delim.LOL","r")
	temp=param.readlines()
	dataname=temp[1].strip()
	
	

	
	
def page1(request):
	form=DropDlist(request.POST)
	form1=uploadfile(request.POST,request.FILES)
	template = "page1.html"
	s="mayank"
	if request.method=='POST':
		print 'form1 yyyyy'	
		
		if 'form11' in request.POST:
			print 'form1 1111'
			if form.is_valid():
				d=int(form.cleaned_data['Select_File'])
				d1=dict(form.fields['Select_File'].choices)[d]
				d1=str(d1)
				str1='echo %s | cat >/root/Desktop/ffff.txt' %d1
				os.system(str1)
				#op=subprocess.Popen(str1,stdout=subprocess.PIPE,shell=True)
				#print op.communicate()[0]
				#print op.communicate()[1]
				#Popen.terminate()
				print "hdfs gfgf %s" % d1
				#sys="hadoop dfsadmin -report"
				#lo=subprocess.Popen(sys,stdout=subprocess.PIPE,shell=True)
				#print lo.communicate()[0]
		
				return HttpResponseRedirect('/page2/')
		elif 'form22' in request.POST:
			print 'form1 2222'
			if form1.is_valid():
				d=form1.cleaned_data['Upload_your_File']
				print 'dddd variable is ',d
				x=d.split('/')
				a=x[len(x)-1]
				a='/'+a
				print 'dddddddddddffff ',a
				str1='echo %s | cat >/root/Desktop/ffff.txt' %a
				os.system(str1)
				print "hdfs %s" %a
				d="hdfs dfs -put %s /" %d
				os.system(d)
				return HttpResponseRedirect('/page2/')
	
	
	#return render(request,template,{'run':s2,'form':form})
	return render(request,template,{'run':s,'form':form,'form1':form1})
	'''s2=""
	form=DropDlist(request.POST)
	form1=uploadfile(request.POST,request.FILES)
	
	if form.is_valid():
		#filename=form.cleaned_data['filename']
		#progname=form.cleaned_data['progname']
		#outputfold=form.cleaned_data['outputfold']
		#print form.cleaned_data['my_choice_field']
		#os.system('hdfs namenode -format')
		#os.system('start-dfs.sh')
		#os.system("hdfs dfs -put /root/Desktop/avc.html /")
		#string="hadoop jar /opt/hadoop-2.6.0/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.6.0.jar %s %s %s" % (progname,filename,outputfold)
		#os.system("hadoop dfsadmin -report")
		d=int(form.cleaned_data['my_choice_field'])
		d1=dict(form.fields['my_choice_field'].choices)[d]
		print "hdfs %s" % d1

	elif form1.is_valid():
		doc=request.POST.get('docfile','')
		#string3="hdfs dfs -put /root/Desktop/%s /" %doc
		#os.system(string3)
		print "filename %s" %doc
		#os.system(string)
		#string1="hdfs dfs -cat %s/part*" %outputfold
		#s1=subprocess.Popen(string1, shell=True, stdout=subprocess.PIPE)
		#temp= s1.communicate()[0]
		
		#for i in temp.split('\n'):
		#	s2=s2+'<br>'+i

	
		
		
	#t=get_template('home.html')
	
	#html=t.render(Context({'run':s2},))
	#return HttpResponse(html)
		#new_join,created=Join.objects.get_or_create(email=email)
		#print new_join,created
		#print new_join.timestamp
		#if created:
			#print "object was created"
		#print filename,progname,outputfold
        #context={"form":form}
	template = "page1.html"
	#return render(request,template,{'run':s2,'form':form})
	return render(request,template,{'form':form,'form1':form1})'''





def page2(request):
	form2=mapred(request.POST)
	form3=mapred1(request.POST,request.FILES)
	template = "page2.html"
	s2=""
	if request.method=='POST':
		f=open("/root/Desktop/ffff.txt",'r')
		k=f.readlines()[0].strip()
		print k
		print 'form1 yyyyy'	
		
		if 'form2' in request.POST:
			print 'form1 2222'
			print request.POST
			#if form2.is_valid():
			map1=request.POST.get('mapper','')
			red1=request.POST.get('reducer','')
			out=request.POST.get('Output_Folder_Name','')
			os.system("rm -rf /root/Desktop/mapred1.txt")
				
			str1="echo 1  >> /root/Desktop/mapred1.txt "
			str3="echo %s  >> /root/Desktop/mapred1.txt " %(out)
			os.system(str1)
			os.system(str3)
			
			print "mapper is %s" %map1
			print "reducer is %s" %red1
			command="hadoop jar /opt/hadoop-2.6.0/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input %s -output %s -mapper /root/Desktop/%s -reducer /root/Desktop/%s" %(k,out,map1,red1)
			
			os.system(command)
			
			return HttpResponseRedirect('/page3/')
			
			#d=int(form.cleaned_data['my_choice_field'])
			#d1=dict(form.fields['my_choice_field'].choices)[d]
			#print "hdfs gfgf %s" % d1
		elif 'form3' in request.POST:
			print 'form1 23332'
			
			
			if form3.is_valid():
				d=form3.cleaned_data['Select_Pre_Built_Program']
				d1=dict(form3.fields['Select_Pre_Built_Program'].choices)[d]
				o=form3.cleaned_data['Output_Folder_Name']
				print "my mapred program is %s" % d1
				
				command="hadoop jar /opt/hadoop-2.6.0/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.6.0.jar %s %s %s " %(d1,k,o)
				#li=subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
				os.system(command)
				#string1="hdfs dfs -cat %s/part*" %o
				#s1=subprocess.Popen(string1, shell=True, stdout=subprocess.PIPE)
				#temp= s1.communicate()[0]
				#print "chal rha h"
				#temp=li.communicate()[0]
				#for i in temp.split('\n'):
				#	s2=s2+'<br>'+i
				#print s2
				os.system("rm -rf /root/Desktop/mapred1.txt")
				
				str1="echo 2  >> /root/Desktop/mapred1.txt "
				
				str3="echo %s  >> /root/Desktop/mapred1.txt " %(o)
				
				os.system(str1)				
				os.system(str3)
								
				return HttpResponseRedirect('/page3/')
				
	
	#template="page2.html"
	#return render(request,template,{'run':s2,'form':form})
	return render(request,template,{'run':s2,'form2':form2,'form3':form3})
	'''form2=mapred(request.POST)
	form3=mapred1(request.POST)
	if form2.is_valid():
		map1=request.POST.get('mapper','')
		red1=request.POST.get('reducer','')

		print request.POST
		print "mapper is %s" %map1
		print "reducer is %s" %red1
		
		
	
	if form3.is_valid():
		d=form3.cleaned_data['my_choice_field']
		print "my mapred program is %s" % d
		
		

	
	template = "page2.html"
	
	return render(request,template,{'form2':form2,'form3':form3})'''

def page4(request):
	print request.POST
	form=DropDlist(request.POST)
	form1=uploadfile(request.POST,request.FILES)
	template = "page1.html"
	if request.method=='POST':
		print 'form1 yyyyy'	
		if form.is_valid():
			d=int(form.cleaned_data['Select_File'])
			d1=dict(form.fields['Select_File'].choices)[d]
			print "hdfs gfgf %s" % d1
		elif 'form22' in request.POST:
			print 'form1 2222'
			if 'form11' in request.POST:
				print 'form1 1111'
			if form1.is_valid():
				d=form1.cleaned_data['Upload_your_File']
				print "hdfs %s" % d
	
	
	#return render(request,template,{'run':s2,'form':form})
	return render(request,template,{'form':form,'form1':form1})



#
			
'''		
def page3(request):
	s2=""
	#if request.method=='POST' or request.method=="GET":
	string1="hdfs dfs -cat %s/part*" %"/output6"
	s1=subprocess.Popen(string1, shell=True, stdout=subprocess.PIPE)
	temp= s1.communicate()[0]
	print "chal rha h"
	#temp=li.communicate()[0]
	for i in temp.split('\n'):
		s2=s2+'<br>'+i
	print s2
		
	#return HttpResponseRedirect('/page2/')
				
	
	template="page2.html"
	#return render(request,template,{'run':s2,'form':form})
	return render(request,template,{'run':s2})'''

def page3(request):
	f=open("/root/Desktop/mapred1.txt",'r')
	k1=f.readlines()
	k=k1[0].strip()
	f1=k1[1].strip()
	template="page3.html"
	html=""
	#fil=f.readlines()[1].strip()
	if str(k)==str('1'):	
		html="http://192.168.43.10:50070/webhdfs/v1%s/part-00000?op=OPEN" % f1
		print html
	elif str(k)==str('2'):
		html="http://192.168.43.10:50070/webhdfs/v1%s/part-r-00000?op=OPEN" % f1
		print html

		
	
	
		
	#output=f.read().strip()

	#html="http://192.168.43.10:50070/webhdfs/v1%s/part-r-00000?op=OPEN" % k
	print html
	return render(request,template,{'run':html})


def hdfs(request):
	template="hdfs.html"
	return render(request,template)

def mapred12(request):
	template="mapred.html"
	return render(request,template)

def status(request):
	template="status.html"
	return render(request,template)



def datanode(request):
	template="datanode.html"
	return render(request,template)



def spage1(request):
	form=DropDlist(request.POST)
	form1=uploadfile(request.POST,request.FILES)
	template = "page1.html"
	s="mayank"
	if request.method=='POST':
		print 'form1 yyyyy'	
		
		if 'form11' in request.POST:
			print 'form1 1111'
			if form.is_valid():
				d=int(form.cleaned_data['Select_File'])
				d1=dict(form.fields['Select_File'].choices)[d]
				d1=str(d1)
				str2='echo 1 | cat >/root/Desktop/choice.txt'
				os.system(str2)
				str1='echo %s | cat >/root/Desktop/ffff1.txt' %d1
				os.system(str1)
				#op=subprocess.Popen(str1,stdout=subprocess.PIPE,shell=True)
				#print op.communicate()[0]
				#print op.communicate()[1]
				#Popen.terminate()
				print "hdfs gfgf %s" % d1
				#sys="hadoop dfsadmin -report"
				#lo=subprocess.Popen(sys,stdout=subprocess.PIPE,shell=True)
				#print lo.communicate()[0]
		
				return HttpResponseRedirect('/spage2/')
		elif 'form22' in request.POST:
			print 'form1 2222'
			if form1.is_valid():
				d=form1.cleaned_data['Upload_your_File']
				str2='echo 2 | cat >/root/Desktop/choice.txt'
				os.system(str2)
				str1='echo %s | cat >/root/Desktop/ffff1.txt' %d
				os.system(str1)
				print "hdfs %s" % d
				return HttpResponseRedirect('/spage2/')
	
	
	#return render(request,template,{'run':s2,'form':form})
	return render(request,template,{'run':s,'form':form,'form1':form1})



def spage2(request):
	form2=sparkmapred(request.POST)
	form3=mapred1(request.POST,request.FILES)
	template = "page2.html"
	s2=""
	if request.method=='POST':
		f1=open("/root/Desktop/choice.txt",'r')
		k1=f1.readlines()[0].strip()		


		f=open("/root/Desktop/ffff1.txt",'r')
		k=f.readlines()[0].strip()
		print k
		print 'form1 yyyyy'	
		
		if 'form2' in request.POST:
			print 'form1 2222'
			print request.POST
			#if form2.is_valid():
			map1=request.POST.get('mapper','')
			
			out=request.POST.get('output','')
			
			
			print "spark bla is %s" %map1
			ss="echo %s >> /root/Desktop/outputn.txt" %out
			os.system(ss)
			command="pyspark SparkWordCount.py"
			
			
			os.system(command)
			ss="hdfs dfs -put /root/Desktop/xyz.txt %s" %o
			os.system(ss)
			return HttpResponseRedirect('/spage3/')
			
			#d=int(form.cleaned_data['my_choice_field'])
			#d1=dict(form.fields['my_choice_field'].choices)[d]
			#print "hdfs gfgf %s" % d1
		elif 'form3' in request.POST:
			print 'form1 23332'
			
			
			if form3.is_valid():
				d=form3.cleaned_data['Select_File']
				d1=dict(form3.fields['Select_File'].choices)[d]
				o=form3.cleaned_data['outputfold']
				print "my mapred program is %s" % d1
				command="pyspark SparkWord1.py"
			
				os.system(command)
				ss="hdfs dfs -put /root/Desktop/xyz.txt %s" %o
				os.system(ss)
				#li=subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
				#string1="hdfs dfs -cat %s/part*" %o
				#s1=subprocess.Popen(string1, shell=True, stdout=subprocess.PIPE)
				#temp= s1.communicate()[0]
				#print "chal rha h"
				#temp=li.communicate()[0]
				#for i in temp.split('\n'):
				#	s2=s2+'<br>'+i
				#print s2
				
				os.system("rm -rf /root/Desktop/mapred1.txt")
				
				str1="echo 2  >> /root/Desktop/mapred1.txt "
				
				str3="echo %s  >> /root/Desktop/mapred1.txt " %(o)
				
				os.system(str1)				
				os.system(str3)
								
				return HttpResponseRedirect('/spage3/')
				
	
	#template="page2.html"
	#return render(request,template,{'run':s2,'form':form})
	return render(request,template,{'run':s2,'form2':form2,'form3':form3})


def spage3(request):
	f=open("/root/Desktop/mapred1.txt",'r')
	k1=f.readlines()
	k=k1[0].strip()
	f1=k1[1].strip()
	template="page3.html"
	html=""
	#fil=f.readlines()[1].strip()
	if str(k)==str('1'):	
		html="http://192.168.43.10:50070/webhdfs/v1%s/part-00000?op=OPEN" % f1
		print html
	elif str(k)==str('2'):
		html="http://192.168.43.10:50070/webhdfs/v1%s/part-r-00000?op=OPEN" % f1
		print html

		
	
	
		
	#output=f.read().strip()

	#html="http://192.168.43.10:50070/webhdfs/v1%s/part-r-00000?op=OPEN" % k
	print html
	return render(request,template,{'run':html})




def testview(request):
	template="D.html"
	w=""
	form=customform3(request.POST)
	if request.method=='POST':
		if form.is_valid():
			stepsize=str(form.cleaned_data['stepsize'])			
			iterations=str(form.cleaned_data['iterations'])
			modelname=str(form.cleaned_data['modelname'])
			command1="sleep 10"
			os.system(command1)

			#comm="spark-submit /root/Desktop/mapredtest1/Godmode/MLModels/linearSGD.py"
			#os.system(comm)
			w="m"
			return HttpResponseRedirect('/modelresult/')
			
	return render(request,template,{'form':form,'w':w})
	




	





		
		
	



