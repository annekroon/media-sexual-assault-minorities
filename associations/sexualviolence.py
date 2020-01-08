#!/usr/bin/env python3

import gensim
import sys
import logging
import re
import os
import json
import itertools
print(sys.executable)
print(sys.version)
import pandas as pd
import argparse

#basepath  = "../../embedding_models/bigrams"
basepath  = "../embeddingmodels/"
#basepath  = "../embedding_models/tabloid/"

parser = argparse.ArgumentParser()
parser.add_argument('--attribute', help='give the attribute (neg or pos)')
parser.add_argument('--target', help='give the target group')
args = parser.parse_args()
attribute = args.attribute
target =    args.target

class word2vec_analyzer():
    '''This class provides a Bias Analyzer for Word2Vec models.'''

    def __init__(self):
        self.nmodel = 0
        self.combinations = []
        with open('../resources/combinations_{}_{}.csv'.format(attribute, target)) as fi:
            for line in fi.readlines():
                self.combinations.append(tuple(line.strip().split(',')))
        logger.info("Created analyzer with {} combinations for {} and {}".format(
            len(self.combinations),target, attribute))


    def get_model(self):
        '''yields a dict with one item. key is the filename, value the gensim model'''
        filenames = [e for e in os.listdir(basepath) if not e.startswith('.')]

        for fname in filenames:
            model = {}
            path = os.path.join(basepath, fname)
            model['gensimmodel'] = gensim.models.Word2Vec.load(path)
            model['filename'] = fname
            splitResult = fname.split( "_" ) #split on scores
            model['doctype'] = splitResult[1]
            model['fromdate'] = splitResult[2]
            model['todate'] = splitResult[3]
            self.nmodel +=1
            yield model

    def get_scores(self):
        results = []
        for model in self.get_model():
            logger.info("Retrieving similarity scores from model {} ...".format(model['filename']))
            for pair in self.combinations:
                try:
                    r = model['gensimmodel'].wv.similarity(pair[0],pair[1])
                    pair_1 = pair[0]
                    pair_2 = pair[1]
                except KeyError:
                    r = 0
                results.append({'pair': (pair[0],pair[1]),
                            'word2vec_score': r,
                            'doctype': model['doctype'],
                            'fromdate': model['fromdate'],
                            'todate': model['todate']})
        return results


if __name__ == "__main__":


    logger = logging.getLogger()
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)

    print("\n\n\nInitiate Analyzer for my dataset\n\n\n")
    myanalyzer = word2vec_analyzer()
    print("\n\n\nCalculate bias scores\n\n\n")
    gensimscore = myanalyzer.get_scores()

    print("\n\n\nSave results\n\n\n")

    df = pd.DataFrame.from_dict(gensimscore)
    print('Created dataframe')
    # print(df)
    df.to_csv('../output/{}_{}_gensimscores.csv'.format(target, attribute))
