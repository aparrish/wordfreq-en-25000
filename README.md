# English word frequency list exported from `wordfreq`

This is a list of 25000 English words and their frequencies, extracted from the
excellent [wordfreq](https://github.com/LuminosoInsight/wordfreq) library. The
list is presented in JSON format, with one large array holding many smaller
arrays with two elements, the first of which is the word and the second of
which is the logarithm of the word's frequency. (To recover the original
frequency fraction, use `math.exp()`.)

I made the list because the `wordfreq` library has [a
dependency](https://pypi.org/project/regex/) without binary builds on
particular platforms, and it's probably easier to distribute this list to my
students than it is to show them how to install a C++ compiler. Hopefully other
people will benefit from the list as well.

Also included in this repository is the (very simple) Python script that I used
to produce this list.

*NOTE:* No effort was made to filter this list to remove words that might be
offensive or inappropriate.

## Sample code

Some quick examples of using the list in Python. This code loads the word list,
and prints out a word's frequency:

```python
wordlist = json.load(open("wordfreq-en-25000-log.json"))
lookup = dict(wordlist)
lookup['allison'] # -12.0892
```

This code shows the word's frequency rank:

```python
wordlist = json.load(open("wordfreq-en-25000-log.json"))
lookup = {row[0]: i for i, row in enumerate(wordlist)}
lookup['allison'] # 10171
```

This code picks words at random from the list, weighted by frequency (requires
numpy):

```python
import numpy as np
wordlist = json.load(open("wordfreq-en-25000-log.json"))
words = [w[0] for w in wordlist]
probs = np.exp([w[1] for w in wordlist])
picked = np.random.choice(word_arr[:,0], p=probs/np.sum(probs), size=14)
print(" ".join(picked))
# example output:
# grow does as cause surprised morning several way said eliminating about september western league
``` 

## License

In accordance with [wordfreq's
license](https://github.com/LuminosoInsight/wordfreq#license), this data is
made available under a [Creative Commons Attribution-ShareAlike 4.0
license](https://creativecommons.org/licenses/by-sa/4.0/). Please see
wordfreq's attributions and documentation for more information about the data
and how it was made.

The little script I used to make the list is hereby released into the public
domain.
