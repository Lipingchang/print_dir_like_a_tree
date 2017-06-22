#!/usr/local/bin/python3.6

import os
#rootname = "/Users" 


# 输出这个路径下的 内容。
def tree(path,show_invisibale=False,deep=0,maxdeep=5,pre='├──'):
	if(deep==0):
		print(path)
	if(deep==maxdeep):
		return
	

	files = os.listdir(path)
	last_out =[]

	# x 是相对路径。 把里面的文件和文件夹分离。 文件夹最后输出。先放到last_out里面。
	for x in files:
		if((x[0]=='.' or x[0]=='~' or x[0]=='$') and not show_invisibale):
			continue
		abspath = os.path.join(path,x)

		if(os.path.isfile(abspath)):
			if(x==files[-1] and len(last_out)==0):
				l = list(pre)
				l[-3] = '└'
				pre = ''.join(l)
			print(pre+x)
		if(os.path.isdir(abspath)):
			last_out.append(x)

	for x in last_out:
		nextpre= pre[0:-3]+'│    '+'├──'
		abspath = os.path.join(path,x)
		if(x==last_out[-1]):
			# 如果是最后一个文件夹的时候，那和上一行的衔接就不应该用 ‘│’ 应该用空格。
			nextpre = pre[0:-3]+'     '+'├──'
			pre = pre[0:-3] + '└' + pre[-2:]
			
		print(pre+'>'+'<'+x+'>')
		tree(abspath,deep=deep+1,maxdeep=maxdeep,pre=nextpre)


rootname = input('enter your dir path:')
rootname = rootname.strip()
maxdeep = input('enter max deep ')
if maxdeep=='':
	maxdeep = 5
else:
	maxdeep = int(maxdeep)
if(os.path.exists(rootname) and os.path.isdir(rootname)):
	tree(rootname,deep=0,maxdeep=maxdeep)


'''
 ├ ─ ─ 

 └ ─ ─  
│ 
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
