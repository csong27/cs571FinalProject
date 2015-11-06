__author__ = 'Song'
import json
from path import Path
from gensim.parsing import *
from labelEmbedding.myWord2Vec import STAR_LABELS
from loadData import yelp_2013_train

STOPWORDS = """
a about across after afterwards against all almost alone along already also although always am among amongst amoungst an and another any anyhow anyone anything anyway anywhere are around as at be
became because become becomes becoming been before beforehand behind being beside besides between beyond both bottom but by call can
cannot cant co computer con could couldnt cry de describe
detail did didn do does doesn doing don done down due during
each eg eight either eleven else elsewhere empty enough etc even ever every everyone everything everywhere except few fifteen
fify fill find fire first for former formerly forty found from front full further get give go
had has hasnt have he hence her here hereafter hereby herein hereupon hers herself him himself his how however hundred i ie
if in inc indeed interest into is it its itself keep last latter latterly ltd
just
kg km
made make many may me meanwhile might mill mine more moreover most mostly move much must my myself name namely
neither never nevertheless next nine no nobody none noone nor not nothing now nowhere of off
often on once only onto or other others otherwise our ours ourselves out over own part per
perhaps please put rather re
quite
rather really regarding
same say see seem seemed seeming seems serious several she should show side since sincere sixty so someone something sometime sometimes somewhere still such system
take ten that the their them themselves then thence there thereafter thereby therefore therein thereupon these they thick thin third this those though through throughout thru thus to together too top toward towards twelve twenty un
until up upon us used using via
was we were what whatever when whence whenever where whereafter whereas whereby wherein whereupon wherever whether which while whither who whoever whole whom whose why will with within without would yet you
your yours yourself yourselves
"""
STOPWORDS = frozenset(w for w in STOPWORDS.split() if w)


def my_remove_stopwords(s):
    s = utils.to_unicode(s)
    return " ".join(w for w in s.split() if w not in STOPWORDS)

DEFAULT_FILTERS = [lambda x: x.lower(), strip_punctuation, strip_multiple_whitespaces, strip_short,
                   strip_numeric, my_remove_stopwords]


class MySentences(object):
    def __init__(self, filename, label=False):
        self.filename = Path(filename)
        self.label = label

    def __iter__(self):
        for line in open(self.filename):
            json_object = json.loads(line)
            text = json_object['text']
            star = json_object['stars']
            if self.label:
                arr = preprocess_string(text, filters=DEFAULT_FILTERS)
                arr.append(STAR_LABELS[int(star) - 1])
                yield arr
            else:
                yield preprocess_string(text, filters=DEFAULT_FILTERS)

if __name__ == '__main__':
    sentences = MySentences(yelp_2013_train, label=True)
