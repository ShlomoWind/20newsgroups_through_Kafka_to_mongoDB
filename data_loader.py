from sklearn.datasets import fetch_20newsgroups

# Define a class to load and return the 20 Newsgroups dataset
class Data:
    def __init__(self):
        self.newsgroups_interesting = interesting_cats=['alt.atheism',
        'comp.graphics',
        'comp.os.ms-windows.misc',
        'comp.sys.ibm.pc.hardware',
        'comp.sys.mac.hardware',
        'comp.windows.x',
        'misc.forsale',
        'rec.autos',
        'rec.motorcycles',
        'rec.sport.baseball']
        self.newsgroups_not_interesting = not_interesting_cats=['rec.sport.hockey',
        'sci.crypt',
        'sci.electronics',
        'sci.med',
        'sci.space',
        'soc.religion.christian',
        'talk.politics.guns',
        'talk.politics.mideast',
        'talk.politics.misc',
        'talk.religion.misc']

# Fetch and return the data for the interesting categories
    def get_newsgroups_interesting(self):
      newsgroups_interesting = fetch_20newsgroups(subset='all', categories=self.newsgroups_interesting)
      return newsgroups_interesting.data

# Fetch and return the data for the not interesting categories
    def get_newsgroups_not_interesting(self):
      newsgroups_not_interesting = fetch_20newsgroups(subset='all', categories=self.newsgroups_not_interesting)
      return newsgroups_not_interesting.data