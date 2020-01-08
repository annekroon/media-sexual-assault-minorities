import gensim
import numpy as np
from itertools import combinations, filterfalse
import math
import logging


logging.getLogger().setLevel(logging.INFO)

path_to_embeddings = '/Users/anne/repos/media-and-sexual-abuse/embedding_models/media-sexual-abuse/models/w2v_adtrouwtelnrcvk_2008_2013'

class WEAT(object):

    def __init__(self):
        self.model = gensim.models.Word2Vec.load(path_to_embeddings)

    def check_vocab(self, word_set):
        missing = [w.lower() for w in word_set if w.lower() not in self.model]
        if missing:
            logging.info('Not in model: {0}'.format(', '.join(missing)))
        return([w.lower() for w in word_set if w.lower() in self.model])

    def check_vocab_sets(self, *word_sets):
        return([self.check_vocab(ws) for ws in word_sets])

    def avg_sim(self, word, word_set):
        similarities = np.array([self.model.similarity(w, word) for w in word_set])
        return(np.mean(similarities))

    def sim_set_diff(self, word, word_set1, word_set2):
        return(self.avg_sim(word, word_set1) - self.avg_sim(word, word_set2))

    def _weat_test(self, tw1, tw2, aw1, aw2):
        targ_sims1 = [self.sim_set_diff(w, aw1, aw2) for w in tw1]
        targ_sims2 = [self.sim_set_diff(w, aw1, aw2) for w in tw2]
        test_stat = sum(targ_sims1) - sum(targ_sims2)
        return(test_stat)

    def _weat_pval(self, tw1, tw2, aw1, aw2):
        test_stat = self._weat_test(tw1, tw2, aw1, aw2)
        observed_over = []
        all_targets = tw1 + tw2
        logging.info('Calculating p val over {2:.0f} length-{0} partitions of {1} words'.format(
            len(tw1), len(all_targets),
            math.factorial(len(all_targets))/
            (math.factorial(len(tw1))*(math.factorial(len(all_targets)-len(tw1))))))
        for c in combinations(all_targets, len(tw1)):
            not_c = filterfalse(lambda x: x in c, all_targets)
            stat = self._weat_test(c, not_c, aw1, aw2)
            observed_over.append(stat > test_stat)
            if len(observed_over) % 1000 == 0:
                logging.info("  Iteration {0}".format(len(observed_over)))
        return(np.mean(observed_over))

    def _weat_effect_size(self, tw1, tw2, aw1, aw2):
        targ_sims1 = np.array([self.sim_set_diff(w, aw1, aw2) for w in tw1])
        targ_sims2 = np.array([self.sim_set_diff(w, aw1, aw2) for w in tw2])
        numerator = np.mean(targ_sims1) - np.mean(targ_sims2)
        denominator = np.std(np.concatenate([targ_sims1, targ_sims2]))
        return(numerator/denominator)

    def weat(self, targ_words1, targ_words2, attr_words1, attr_words2):
        tw1, tw2, aw1, aw2 = self.check_vocab_sets(targ_words1, targ_words2, attr_words1, attr_words2)
        test_stat = self._weat_test(tw1, tw2, aw1, aw2)
        pval = self._weat_pval(tw1, tw2, aw1, aw2)
        effect_size = self._weat_effect_size(tw1, tw2, aw1, aw2)
        return([test_stat, pval, effect_size])

weat_analyzer = WEAT()
print("Loading model... ")

aangenaam = ["vrijheid", "gezondheid", "liefde", "vrede", "gejuich", "vriend", "hemel", "loyaal", "plezier", "diamant", "zachtaardig" , "eerlijk", "gelukkig", "regenboog", "diploma", "geschenk", "eer", "wonder", "zonsopgang", "familie",
"gelukkig", "gelach", "paradijs", "vakantie"]
aangenaam = aangenaam[:21]

print("This is the length of the attributes 'Aangenaam': {}".format(len(aangenaam)))
sexual_threat = [line.strip().lower() for line in open('../resources/attributes/negative.txt').readlines() if len(line)>1]

print("This is the length of the attributes 'Sexual Threat': {}".format(len(sexual_threat)) )

arabic = [line.strip().lower() for line in open('../resources/targets/arabic_firstnames.txt').readlines() if len(line)>1]

dutch = [line.strip().lower() for line in open('../resources/targets/dutch_firstnames.txt').readlines() if len(line)>1]

ara = arabic [:2]
dut = dutch [:2]
a = aangenaam[:2]
b = sexual_threat[:2]


results = weat_analyzer.weat(arabic, dutch, sexual_threat, aangenaam)

with open('../output/results_weat.txt', 'w') as filehandle:
    for listitem in results:
        filehandle.write('%s\n' % listitem)
