#!/usr/bin/env python3

'''
This script reads some files with words (attributes and target groups)
and creates a new file with combinations of those

'''

import itertools

neg = [line.strip().lower() for line in open('../resources/attributes/negative.txt').readlines() if len(line)>1]
pos  = [line.strip().lower() for line in open('../resources/attributes/positive.txt').readlines() if len(line)>1]
arab  = [line.strip().lower() for line in open('../resources/targets/arabic_firstnames.txt').readlines() if len(line)>1]
dutch= [line.strip().lower() for line in open('../resources/targets/dutch_firstnames.txt').readlines() if len(line)>1]
nat = [line.strip().lower() for line in open('../resources/targets/nationalities.txt').readlines() if len(line)>1]
af = [line.strip().lower() for line in open('../resources/targets/africa.txt').readlines() if len(line)>1]
eur = [line.strip().lower() for line in open('../resources/targets/europa.txt').readlines() if len(line)>1]
refugees = [line.strip().lower() for line in open('../resources/targets/refugees_.txt').readlines() if len(line)>1]
ingroup = [line.strip().lower() for line in open('../resources/targets/ingroup.txt').readlines() if len(line)>1]

print(refugees)

# remove duplicates

neg = set(neg)
pos = set(pos)
arab = set(arab)
dutch = set(dutch)
nat = set(nat)
af = set(af)
eur = set(eur)
refugees  = set(refugees)
ingroup = set(ingroup)



pairs_neg_arab = list(itertools.product(neg,arab))
pairs_neg_dutch = list(itertools.product(neg,dutch))
pairs_neg_nat = list(itertools.product(neg,nat))
pairs_pos_arab = list(itertools.product(pos,arab))
pairs_pos_dutch = list(itertools.product(pos,dutch))
pairs_pos_nat = list(itertools.product(pos,nat))
pairs_pos_af = list(itertools.product(pos,af))
pairs_neg_af = list(itertools.product(neg,af))

pairs_pos_eur = list(itertools.product(pos,eur))
pairs_neg_eur = list(itertools.product(neg,eur))

pairs_pos_refugees = list(itertools.product(pos,refugees))
pairs_neg_refugees = list(itertools.product(neg,refugees))
#print(pairs_pos_ref, pairs_neg_ref)

pairs_pos_ingroup = list(itertools.product(pos,ingroup))
pairs_neg_ingroup = list(itertools.product(neg,ingroup))

with open('../resources/combinations_neg_arab.csv',mode='w') as fo:
    for pair in pairs_neg_arab :
        fo.write("{},{}\n".format(pair[0],pair[1]))

with open('../resources/combinations_neg_dutch.csv',mode='w') as fo:
    for pair in pairs_neg_dutch :
        fo.write("{},{}\n".format(pair[0],pair[1]))
        
with open('../resources/combinations_pos_dutch.csv',mode='w') as fo:
    for pair in pairs_pos_dutch:
        fo.write("{},{}\n".format(pair[0],pair[1]))

with open('../resources/combinations_pos_arab.csv',mode='w') as fo:
    for pair in pairs_pos_arab:
        fo.write("{},{}\n".format(pair[0],pair[1]))
        
with open('../resources/combinations_pos_nat.csv',mode='w') as fo:
    for pair in pairs_pos_nat:
        fo.write("{},{}\n".format(pair[0],pair[1]))

with open('../resources/combinations_neg_nat.csv',mode='w') as fo:
    for pair in pairs_neg_nat :
        fo.write("{},{}\n".format(pair[0],pair[1]))
        
with open('../resources/combinations_pos_af.csv',mode='w') as fo:
    for pair in pairs_pos_af:
        fo.write("{},{}\n".format(pair[0],pair[1]))

with open('../resources/combinations_neg_af.csv',mode='w') as fo:
    for pair in pairs_neg_af :
        fo.write("{},{}\n".format(pair[0],pair[1]))
        
        
with open('../resources/combinations_pos_eur.csv',mode='w') as fo:
    for pair in pairs_pos_eur:
        fo.write("{},{}\n".format(pair[0],pair[1]))

with open('../resources/combinations_neg_eur.csv',mode='w') as fo:
    for pair in pairs_neg_eur :
        fo.write("{},{}\n".format(pair[0],pair[1]))
        
        
with open('../resources/combinations_pos_ref.csv',mode='w') as fo:
    for pair in pairs_pos_refugees:
        fo.write("{},{}\n".format(pair[0],pair[1]))

with open('../resources/combinations_neg_ref.csv',mode='w') as fo:
    for pair in pairs_neg_refugees:
        fo.write("{},{}\n".format(pair[0],pair[1]))
        
        
with open('../resources/combinations_pos_ingroup.csv',mode='w') as fo:
    for pair in pairs_pos_ingroup:
        fo.write("{},{}\n".format(pair[0],pair[1]))

with open('../resources/combinations_neg_ingroup.csv',mode='w') as fo:
    for pair in pairs_neg_ingroup :
        fo.write("{},{}\n".format(pair[0],pair[1]))