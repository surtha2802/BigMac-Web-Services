import os

data=open("/root/Desktop/modelsaves.LOL","r")
temp=data.readlines()
os.system("rm -rf /root/Desktop/mpv2/mapredtest1/templates/modelsav.html")
o=open("/root/Desktop/mpv2/mapredtest1/templates/modelsav.html","w")

o.write("<html>")
o.write("<body>")
o.write("\n")
for i in range(0,len(temp)):
	c=r"<a href='http://192.168.43.10:50070/webhdfs/v1/%s.tar.gz?op=OPEN'>%s</a>"%(temp[i],temp[i])
	o.write(c)
	o.write("<br>")
	
o.write("</body>")
o.write("</html>")















