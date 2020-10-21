import wordfreq
import math
import json

wordlist = [(w, round(math.log(wordfreq.word_frequency(w, 'en')), 4)) 
        for w in wordfreq.top_n_list("en", 25000)]

with open("wordfreq-en-25000-log.json", "w") as fh:
    json.dump(wordlist, fh, indent=2)

