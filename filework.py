import re
#import win32gui

tracka = []
file = open('tracks.txt','r',encoding='utf8',errors='ignore')
fire = open("ready.txt","w")

while True:
	content=file.readline()
	if not content:
		break
	x = re.findall("PC\\d{9}BY", content)
	if x:
		tracka.append(x)
		fire.write(str(x[0])+"\n")
	#	print(type(x))
	#print(content)
	#print(x)
file.close()
fire.close()

#fire = open("ready.txt","w")
#for i in tracka:
#    fire.write(str(i[0])+"\n")
#fire.close
