from django.shortcuts import render
import os
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
import subprocess
def home(request):
	p=os.system("ls > /root/Desktop/avc.txt")
	print p	
	#k="awk '{print $0\"<br>\"}' /root/Desktop/avc.txt >/root/Desktop/avccon.txt"
	os.system("")
	f= open('/root/Desktop/avc.txt','r')
	#p=subprocess.Popen(['ls'], shell=True,stdout=subprocess.PIPE)
	#r= p.communicate()[0]
	a= f.readlines()
	s=""
	for i in range(0,len(a)):
		s=s+'<br>'+str(a[i])
		s=s+''
	#r="<p> bjbj<p>"
	t=get_template('home.html')
	html=t.render(Context({'run':s}))
	return HttpResponse(html)







