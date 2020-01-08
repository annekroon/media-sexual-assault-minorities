
#!/usr/bin/env python3

'''
This script reads some files with words (attributes and target groups)
and creates a new file with combinations of those

'''

PATH = "/home/anne/tmpanne/"
#FILENAME = "uniekezinnen_1991-01-01_2018-12-31"
FILENAME = "uniekezinnen_1991-01-01_2018-12-31_ad_trouw"
FILE_CLEAN = "uniekezinnen_1991-01-01_2018-12-31_ad_trouw_clean"

documents = [line.strip() for line in open(FILENAME, 'r+', encoding="utf-8").readlines() if len(line)>1 and len(line)< 200]
stopwords = [line.strip() for line in open('../stopwords/stopwords_NL.txt', 'r+', encoding="utf-8").readlines() if len(line)>1]

text_clean = [" ".join([w for w in speech.split() if w not in mystopwords]) for speech in documents]

with open(FILE_CLEAN, mode='w') as fo:
    for sentence in text_clean:
        fo.write(sentence)
        fo.write('\n')