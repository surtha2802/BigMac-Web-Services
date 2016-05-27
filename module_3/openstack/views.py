from django.shortcuts import render
from .forms import DropDlist
from django.template import Context
from django.template.loader import get_template

from django.http import HttpResponse,HttpResponseRedirect
import os,subprocess
def Home(request):
	template="Home.html"
	if request.method=='POST':
		print 'form1 yyyyy'	
		
		if 'form11' in request.POST:
			print 'form1 1111'
			
			
	
			return HttpResponseRedirect('/opage1/')
		elif 'form22' in request.POST:
			print 'form1 2222'
			return HttpResponseRedirect('/opage2/')

	return render(request,template)
def opage1(request):
	print "kkll"
	farzi="--os-username admin --os-password prax --os-tenant-name admin --os-auth-url http://192.168.43.154:35357/v2.0/"
	command="nova  %s list  > /root/Desktop/av_os_list.txt" %farzi
	os.system(command)
	f=open("/root/Desktop/av_os_list.txt","r")
	k=f.readlines()[3:]
	k=k[:len(k)-1]
	OS=20*['']

	count=0
	for i in range(0,len(k)):
		temp=k[i].split('|')[2].strip()
		count=count+1
		OS[i]=(temp+'.jpg')
		#OS[i]=('<input type=image src="{% static /img/'+temp+'.jpg %}">')


#	if request.method=='POST':
	print 'cirros yyyyy',request.POST	
	s1=''
	if 'Cirros' in request.POST:
		c1="echo Cirros > /root/Desktop/osname.txt"
		os.system(c1)
		print 'Cirros 1111'
		#nova get-vnc-console INSTANCE_NAME VNC_TYPE
		start1= "nova %s start Cirros" %farzi 
		os.system(start1)
		os.system("sleep 5")
		command="nova %s get-vnc-console Cirros novnc > /root/Desktop/osurl.txt" %farzi
		print command
		os.system(command)
		os.system("rm -rvf /root/Desktop/myproject/static/static_dirs/img/CirrosQR.jpg")
		os.system("rm -rvf /root/Desktop/myproject/static/static_root/img/CirrosQR.jpg")
		f= open('/root/Desktop/osurl.txt','r')
		temp=f.readlines()[3].split('|')[2].strip()
		command="qrencode -o /root/Desktop/myproject/static/static_dirs/img/CirrosQR.jpg %s" %temp
		os.system(command)
		os.system("echo yes| python /root/Desktop/myproject/manage.py collectstatic")
		s1="echo 1 > /root/Desktop/qrno.txt"
		os.system(s1)
		
		

		return HttpResponseRedirect('/opage3/')
	elif 'Kolibri' in request.POST:
		c1="echo Kolibri > /root/Desktop/osname.txt"
		os.system(c1)
		print 'Kolibri 2222'
		start1= "nova %s start Kolibri" %farzi
		os.system(start1)
		os.system("sleep 5")
		command="nova %s get-vnc-console Kolibri novnc > /root/Desktop/osurl.txt" %farzi
		os.system(command)
		os.system("rm -rvf /root/Desktop/myproject/static/static_dirs/img/KolibriQR.jpg")
		os.system("rm -rvf /root/Desktop/myproject/static/static_root/img/KolibriQR.jpg")
		f= open('/root/Desktop/osurl.txt','r')
		temp=f.readlines()[3].split('|')[2].strip()
		command="qrencode -o /root/Desktop/myproject/static/static_dirs/img/KolibriQR.jpg %s" %temp
		os.system(command)
		os.system("echo yes | python /root/Desktop/myproject/manage.py collectstatic")
		s1="echo 2 > /root/Desktop/qrno.txt"
		os.system(s1)
		return HttpResponseRedirect('/opage3/')
	
	elif 'Ubuntu' in request.POST:
		c1="echo Ubuntu > /root/Desktop/osname.txt"
		os.system(c1)
		print 'Ubuntu 2222'
		start1= "nova %s start Ubuntu" %farzi
		os.system(start1)
		command="nova %s get-vnc-console Ubuntu novnc > /root/Desktop/osurl.txt" %farzi
		os.system(command)
		os.system("rm -rvf /root/Desktop/myproject/static/static_dirs/img/UbuntuQR.jpg")
		os.system("rm -rvf /root/Desktop/myproject/static/static_root/img/UbuntuQR.jpg")
		f= open('/root/Desktop/osurl.txt','r')
		temp=f.readlines()[3].split('|')[2].strip()
		command="qrencode -o /root/Desktop/myproject/static/static_dirs/img/UbuntuQR.jpg %s" %temp
		os.system("echo yes | python /root/Desktop/myproject/manage.py collectstatic")
		os.system(command)
		s1="echo 3 > /root/Desktop/qrno.txt"
		os.system(s1)
		
		return HttpResponseRedirect('/opage3/')

	template="opage1.html"
	#return HttpResponse(getImg.simple(),mimetype="image/png")
	return render(request,template,)

def opage2(request):
	form=DropDlist(request.POST)
	template="customOS.html"
	if request.method=='POST':
		print 'form1 yyyyy'	
		print request.POST,'kkkllll'
		
		if 'Create_os' in request.POST:
			print 'form1 os os '
			if form.is_valid():
				farzi="--os-username admin --os-password prax --os-tenant-name admin --os-auth-url http://192.168.43.154:35357/v2.0/"
				name=form.cleaned_data['OS_Name']
				d=int(form.cleaned_data['Image_To_Boot'])
				d1=dict(form.fields['Image_To_Boot'].choices)[d]
				d1=str(d1).strip()
				
				c1="echo %s > /root/Desktop/osname.txt" %name
				os.system(c1)

				r=int(form.cleaned_data['Flavor_List'])
				r1=dict(form.fields['Flavor_List'].choices)[r]
				r1=str(r1).strip()

				netid='8d411659-d5b5-4560-9b5b-36637ab72f89'
				command='nova %s boot --image %s --flavor %s  --nic net-id=%s %s' %(farzi,d1,r1,netid,name)
				os.system(command)
				
				command2="nova %s list" % farzi

				s=subprocess.Popen(["nova --os-username admin --os-password prax --os-tenant-name admin --os-auth-url http://192.168.43.154:35357/v2.0/ list"],stdout=subprocess.PIPE, shell=True)
				temp=s.communicate()[0]

				print temp,'dsfsdf'
				temp=temp.split('\n')
				temp1=temp[3:]
				temp2=temp1[:len(temp1)-2]

				i=True
				
				while i:
	
					for i in temp2:
		
						if str(i.split('|')[2].strip())==name and str(i.split('|')[3].strip())=='ACTIVE':
							i=False
							#print "HOt & juicy Choot"
							break

						elif str(i.split('|')[2].strip())==name and str(i.split('|')[3].strip())=='ERROR':
							print "LODA"
							i=False
							break
						else:
							print "hjgj"
							s=subprocess.Popen(["nova --os-username admin --os-password prax --os-tenant-name admin --os-auth-url http://192.168.43.154:35357/v2.0/ list"],stdout=subprocess.PIPE, shell=True)
							temp=s.communicate()[0]
							temp=temp.split('\n')
							temp1=temp[3:]
							temp2=temp1[:len(temp1)-2]
							#print str(i.split('|')[2].strip()),str(i.split('|')[4].strip())
							continue
		
	


						
				command1="nova %s get-vnc-console %s novnc > /root/Desktop/osurl.txt" %(farzi,name)
				os.system(command1)	
				os.system("rm -rvf /root/Desktop/myproject/static/static_dirs/img/CustomQR.jpg")
				os.system("rm -rvf /root/Desktop/myproject/static/static_root/img/CustomQR.jpg")
				f= open('/root/Desktop/osurl.txt','r')
				temp=f.readlines()[3].split('|')[2].strip()
				command="qrencode -o /root/Desktop/myproject/static/static_dirs/img/CustomQR.jpg %s" %temp
				os.system(command)
				os.system("echo yes | python /root/Desktop/myproject/manage.py collectstatic")
				#op=subprocess.Popen(str1,stdout=subprocess.PIPE,shell=True)
				#print op.communicate()[0]
				#print op.communicate()[1]
				#Popen.terminate()
				#print "hdfs gfgf %s" % d1
				#sys="hadoop dfsadmin -report"
				#lo=subprocess.Popen(sys,stdout=subprocess.PIPE,shell=True)
				#print lo.communicate()[0]
		
				return HttpResponseRedirect('/opage3/')

	return render(request,template,{'form':form})

def opage3(request):
	template="opage3.html"
	f= open('/root/Desktop/osurl.txt','r')
	temp=f.readlines()[3].split('|')[2].strip()
	#html='<iframe src=%s  heigth=2000px width=1000px></iframe>' %temp
	#print html
	return render(request,template,{'run':temp})

def qrcode(request):
	print "aaya"
	
	f1=open('/root/Desktop/osname.txt','r')
	temp1=f1.read().strip()
	print temp1
	print "running"
	if temp1=="Cirros":
		print "1"
		template="Cirros.html"
		return render(request,template)
	elif temp1=="Kolibri":
		print "2"
		template="Kolibri.html"
		return render(request,template)
	elif temp1=="Ubuntu":
		print "3"
		template="Ubuntu.html"
		return render(request,template)
	else:
		print "4"
		template="Custom.html"
		return render(request,template)

def overv(request):
	template="overview.html"
	return render(request,template)

def default(request):
	template="default.html"
	return render(request,template)

	


