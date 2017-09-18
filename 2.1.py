# -*- coding: utf-8 -*-
import os
import os.path

filepaths=[]
for root,dirs,files in os.walk("D:\\bigdata\\2.1\\SogouC.mini\\Sample"):
    for name in files:
        filepaths.append(os.path.join(root,name))


import codecs
filepaths=[]
filecotents=[]
for root,dirs,files in os.walk("D:\\bigdata\\2.1\\SogouC.mini\\Sample"):
    for name in files:
        filepath=os.path.join(root,name)
        filepaths.append(filepath)
        f=codecs.open(filepath,'r','utf-8')
        filecontents=f.read()
        f.close()
import pandas
corpos=pandas.DataFrame({'filePath':filepaths,
                         'fileContent':filecontents})
                         
                         