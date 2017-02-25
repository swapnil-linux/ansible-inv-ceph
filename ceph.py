#!/usr/bin/python
#
# (c) 2017 Swapnil Jain <swapnil@linux.com>
#          Nirmit Patel <nirmit@mask365.com>
#          
# Ansible dynamic inventory script to list of CEPH nodes grouped by mon, osd & mds

import os
import sys
import json

from subprocess import Popen, PIPE
result={}
p2 = Popen(["ceph", "node", "ls"], stdout=PIPE)
output = p2.communicate()[0]

data = json.loads(output)
#with open('sampleinput') as data_file:    
#	data = json.load(data_file)
try:
	mons=data['mon'];
	monvalues=mons.keys()
	result['mon']=monvalues
except:
	result['mon']=[]

try:
	osds=data['osd'];
	osdvalues=osds.keys()
	result['osd']=osdvalues
except:
	result['osd']=[]

try:
	mdss=data['mds'];
	mdsvalues=mdss.keys()
	result['mds']=mdsvalues
except:
	result['mds']=[]
print json.dumps(result)


