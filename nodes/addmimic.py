#!/usr/bin/env python

import os
import os.path
import urllib
import requests
from requests.auth import HTTPBasicAuth

import time

auth = HTTPBasicAuth('', 'ROS')
videodir = "/home/jll/common"
url = "http://localhost:8080/requests/status.xml"

time.sleep(2)

# todo waiting for vlc start

for parent, dirnames, filenames in os.walk(videodir):
    for filename in filenames:
		# print os.path.join(parent,filename)
        fullurl = url + '?' + urllib.urlencode(dict(command="in_enqueue", input=os.path.join(parent,filename)))
        requests.get(fullurl, auth=auth)