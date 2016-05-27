from django.shortcuts import render
from .forms import DropDlist,uploadfile,mapred,mapred1,sparkmapred
from django.template import Context
from django.template.loader import get_template

from django.http import HttpResponse,HttpResponseRedirect
import os,subprocess

def index(request):
	template="index.html"
	return render(request,template)

def bigdash(request):
	template="mapred-home.html"
	return render(request,template)

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




	





		
		
	



