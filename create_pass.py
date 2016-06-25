#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import random,string
import re

#chk parament
if len(sys.argv) < 2:
    print ('\nUsage: python %s <number>') % sys.argv[0]
    print ('e.g. : python %s 16\n') % sys.argv[0]
    sys.exit()

Val = sys.argv[1]
pat = re.compile('\D')

#chk parament type
if pat.findall(Val):
    print('Pls input number bigger zero.\n')
    sys.exit()
else:
   passLen = int(Val) 

#passwd string
strs = string.printable
strsNew = re.findall('\S', strs)
#print len(strsNew)
passStr = ''
for x in range(passLen):
    x += 1
    passStr += strsNew[random.randrange(len(strsNew))]
print('\nPassword: '+passStr+'\n')
