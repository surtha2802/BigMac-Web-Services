def get_my_choices():
	import subprocess
	string="hdfs dfs -ls /"
	l=[]	
	j=1
	s=subprocess.Popen(string,stdout=subprocess.PIPE,shell=True)
	string1="ls"
	s1=subprocess.Popen(string1,stdout=subprocess.PIPE,shell=True)
	print "lololololol  %s" %(s1.communicate()[0])
	st=s.communicate()[0].split('\n')[1:]
	st=st[:len(st)-1]
	for i in st:
		print i.split(' ')	
		temp=i.split(' ')
		z= temp[len(temp) -1]
		print type(temp)	
		l.append((j,z))
		j=j+1
	return l
