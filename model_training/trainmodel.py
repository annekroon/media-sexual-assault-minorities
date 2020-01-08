import gensim
import logging
import re
import itertools
from gensim.models import Phrases
from gensim.models.phrases import Phraser
import nltk
import csv
import string
from gensim.models import Word2Vec
from nltk.corpus import stopwords
#import nltk
#nltk.download('punkt')

#from nltk import word_tokenize,sent_tokenize
#import nltk

print("LETS DO THIS")

lettersanddotsonly = re.compile(r'[^a-zA-Z\.]')
PATH = "/home/anne/tmpanne/media-sexual-abuse/"
#FILENAME = "uniekezinnen_1991-01-01_2018-12-31"
FILENAME = "uniekezinnen_2014-01-01_2018-12-31_ad_trouw"

stopWords = stopwords.words('dutch')
#sentences_all = [line.strip() for line in open(FILENAME).readlines() if len(line)>1]
#sentences_clean = [" ".join([w for w in sentence.split() if w not in stopWords]) for sentence in sentences_all]

W2V_PARAMETERS = {'size': 300,
    'window': 10,
    'negative': 5
}

def preprocess(s):
    s = s.lower().replace('!','.').replace('?','.')  # replace ! and ? by . for splitting sentences
    s = lettersanddotsonly.sub(' ',s)
    return s

class train_model():

    def __init__(self, fromdate,todate):
        self.fromdate = fromdate
        self.todate = todate
        print('Start reading sentences')
       	documents = [line.strip() for line in open(PATH + FILENAME).readlines() if len(line)>1 and len(line)< 200]
       	sentences = [" ".join([w for w in sentence.split() if w not in stopWords]) for sentence in documents]
        print("start tokenization...")
        #self.corpus =  [nltk.word_tokenize(sentence) for sentence in self.sentences]
        self.corpus = [x.split(" ") for x in sentences]
        
       	#print('Start tokenization')
      #  self.corpus = [nltk.word_tokenize(sentence) for sentence in self.sentences]
        #print("CORPUS", self.corpus)
        print('Start phrases')
        self.phrases = Phrases(sentences=self.corpus,min_count=25,threshold=50)
        self.bigram = Phraser(self.phrases)
       # for sent in self.bigram[self.sentences]:  # apply model to text corpus
        #    pass

        for index, sentence in enumerate(self.corpus):
            self.corpus[index] = self.bigram[sentence]
       
        self.model = gensim.models.Word2Vec(**W2V_PARAMETERS)
        self.model.build_vocab(self.corpus)		
        
        print('Build Word2Vec vocabulary')
        self.model.train(self.corpus,total_examples=self.model.corpus_count, epochs=self.model.iter)
        print('Estimated Word2Vec model')
        
def train_and_save(fromdate,todate):
    filename = "{}w2v_timeframe1".format(PATH + FILENAME)

    casus = train_model(fromdate,todate)

    with open(filename, mode='wb') as fo:
        casus.model.save(fo)
    print('Saved model')
    print("reopen it with m = gensim.models.word2vec.load('{}')".format(filename))
    del(casus)

if __name__ == "__main__":

    logger = logging.getLogger()
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)

    train_and_save(fromdate = "2000-01-01", todate = "2017-12-31")
