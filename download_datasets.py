
import wget
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

dirNames = ['data' ,  'data/raw' , 'embeddingmodels']

for i in dirNames:
    try:
        os.mkdir(i)
        print("Directory " , i ,  " Created ")
    except FileExistsError:
        print("Directory " , i ,  " already exists")

# get embedding models:

[wget.download(i, 'embeddingmodels') for i in ["https://osf.io/tmdz6/download", "https://osf.io/493w7/download" ] ]

# get media attention files:

[wget.download(i, 'data/raw') for i in ["https://osf.io/u3hm7/download", "https://osf.io/3uzqy/download", "https://osf.io/65h2n/download" ] ]
