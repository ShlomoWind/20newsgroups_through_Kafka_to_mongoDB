from sklearn.datasets import fetch_20newsgroups

# Define a class to load and return the 20 Newsgroups dataset
class Data:
    def __init__(self):
        self.interesting_cats=['alt.atheism',
        'comp.graphics',
        'comp.os.ms-windows.misc',
        'comp.sys.ibm.pc.hardware',
        'comp.sys.mac.hardware',
        'comp.windows.x',
        'misc.forsale',
        'rec.autos',
        'rec.motorcycles',
        'rec.sport.baseball']
        self.not_interesting_cats=['rec.sport.hockey',
        'sci.crypt',
        'sci.electronics',
        'sci.med',
        'sci.space',
        'soc.religion.christian',
        'talk.politics.guns',
        'talk.politics.mideast',
        'talk.politics.misc',
        'talk.religion.misc']
        self.interesting_data = fetch_20newsgroups(subset='all', categories=self.interesting_cats)
        self.not_interesting_data = fetch_20newsgroups(subset='all', categories=self.not_interesting_cats)
        self.idx = 0

# Method to get batches of interesting and not interesting data
    def get_data(self):
        starter = self.idx
        end = self.idx + 10
        interesting_batch = self.interesting_data.data[starter:end]
        not_interesting_batch = self.not_interesting_data.data[starter:end]
        self.idx = end
        if self.idx >= len(self.interesting_data.data) or self.idx >= len(self.not_interesting_data.data):
            self.idx = 0
        return interesting_batch, not_interesting_batch