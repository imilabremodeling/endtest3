import os

fp = open("a.txt","a")
for i in range(100):
	temp = str(i)+"\n"
	fp.write(temp)
	
fp.close()	

