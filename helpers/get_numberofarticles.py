#!/usr/bin/env python3
import json
import os
import glob
import pandas as pd

timeframes = ['2008_2013', '2014_2018']
for i in timeframes:
    path_to_jsonfiles = '../embeddingmodels/w2v_adtrouwtelnrcvk_{}_nrarticles.json'.format(i)

    full_filename = "{}".format(path_to_jsonfiles)
    with open(full_filename,'r') as fi:
        mydict = json.load(fi)

    df = pd.DataFrame(mydict)
    df.to_csv('../output/nr_articles_{}.csv'.format(i))
