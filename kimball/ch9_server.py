# -*- coding: utf-8 -*-
"""
Created on Sun May  7 13:13:21 2017

@author: Wu
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May  7 01:46:58 2017

@author: Wu
"""
import os
##prepare 
os.chdir('c:/coding/intro_python/kimball')
if not os.path.isdir('templates'):
    os.mkdir('templates')

homeTemp='''<html>
<head>
<title>It's alive!</title>
<body>
I'm of course referring to {{thing}}, which is {{height}} feet tall and {{color}}.
</body>
</html>'''

with open('templates/home.html','w') as inFile:
    inFile.write(homeTemp)
    
with open('index.html','w') as inFile:
    inFile.write("it's alive!")
#%%

#set up
from flask import Flask, render_template, request
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    thing = request.args.get('thing')
    height = request.args.get('height')
    color = request.args.get('color')
    
    if not thing and not height and not color:
        return app.send_static_file('index.html')
    else:
        return render_template('home.html',thing=thing, height=height,color=color)
    
app.run(port=9999, debug=True)