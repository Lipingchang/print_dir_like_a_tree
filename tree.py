#!/usr/local/bin/python3.6

import os
rootname = "/Users/luo-banqi/Desktop" 
#for x in os.walk(rootname):
#	print(x)
#print(os.listdir(rootname))



# 输出这个路径下的 内容。
def tree(path,deep=0,maxdeep=5,show_invisibale=False):
	if(deep==0):
		print(path)
	if(deep==maxdeep):
		return
	pre = deep*'│   '+'├── '

	pre2= deep*'│   '+'└── '

	files = os.listdir(path)
	last_out =[]

	# x 是相对路径。
	for x in files:
		abspath = os.path.join(path,x)
		if((x[0]=='.' or x[0]=='~') and not show_invisibale):
			continue

		if(os.path.isfile(abspath)):
			if(x==files[-1] and len(last_out)==0):
				pre = pre2
			print(pre+x)
		if(os.path.isdir(abspath)):
			last_out.append(x)

	for x in last_out:
		abspath = os.path.join(path,x)
		if(x==last_out[-1]):
			pre = pre2
		print(pre+'>'+x)
		tree(abspath,deep+1)

tree(rootname,0,5)

'''
 ├ ─ ─ 

 └ ─ ─  

 ├── aaaaa
    ├── aaa-2-inin
    ├── aaa-ininin
      └──sdf2.txt
   └──sdf.txt

├── aaaaa
    ├── aaa-2-inin
    ├── aaa-ininin
      └──sdf2.txt
   └──sdf.txt'''
