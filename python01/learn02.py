with open('E:/learnpython/python01/testio.txt','r') as f:
	print("--------",f.read())

with open('E:/learnpython/python01/testio.txt','r') as s:
	for line in s.readlines():
		print(".....",line.strip())

		
from io import StringIO

m=StringIO()
m.write('hello')
m.write(' ')
m.write('world!')
print(m.getvalue())

import os
print(os.name)
print(os.environ)
print(os.environ.get('PATH'))

print(os.path.abspath('.'))

listdir = [x for x in os.listdir('.') if os.path.isdir(x)]
print(listdir)

listdir = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(listdir)


import pickle

d=dict(name='Bob',age=20,score=88)
print(pickle.dumps(d))

with open('E:/learnpython/python01/testio01.txt','rb') as n:
	d = pickle.load(n)
	print(d)
	
import json
d = dict(name="MIKE",age=90,score=90)
print(json.dumps(d))


from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))




