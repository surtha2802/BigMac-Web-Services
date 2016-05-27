from django.shortcuts import render
from .forms import EmailForm
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
import os,subprocess
def home(request):
	s2=""
	form=EmailForm(request.POST or None)
	
	if form.is_valid():
		filename=form.cleaned_data['filename']
		progname=form.cleaned_data['progname']
		outputfold=form.cleaned_data['outputfold']
		
		#os.system('hdfs namenode -format')
		#os.system('start-dfs.sh')
		#os.system("hdfs dfs -put /root/Desktop/avc.html /")
		#string="hadoop jar /opt/hadoop-2.6.0/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.6.0.jar %s %s %s" % (progname,filename,outputfold)
		#os.system(string)
		string1="hdfs dfs -cat %s/part*" %outputfold
		s1=subprocess.Popen(string1, shell=True, stdout=subprocess.PIPE)
		temp= s1.communicate()[0]
		
		for i in temp.split('\n'):
			s2=s2+'<br>'+i
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
	template = "home.html"
	return render(request,template,{'run':s2,'form':form})


# Create your views here.
