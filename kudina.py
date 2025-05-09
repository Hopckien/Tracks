import re
#import io

file = open("tracks.txt","r",encoding="utf-8",errors='ignore')
while True:
	content=file.readline()
	if not content:
		break
	print(content)
file.close()
