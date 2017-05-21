# -*- coding: utf-8 -*-
"""
Created on Sun May  7 01:46:58 2017

@author: Wu
"""
import os
import subprocess
import signal
import requests
import time

os.chdir('c:/coding/intro_python/kimball')

#9.1
call=subprocess.Popen('python ch9_server.py',shell=True)
res=requests.get('http://localhost:9999')
print(res.text)

#9.2
res=requests.get('http://localhost:9999?thing=the%20furious%20monster&height=50&color=colored%20shining%20black')
print(res.text)
#call.send_signal(signal.SIGTERM)
call.kill()
print(call.returncode)

