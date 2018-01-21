import math

def _calculate_distance(word):
    try:
        return sum(map(lambda x: math.log(ord(x), 10) ** word.index(x), word)) ** 0.8
    except:
        return -1

def mbsearch(seq, t):
    min = 0
    max = len(seq) - 1
    while True:
        if max < min:
            return m
        m = (min + max) // 2
        if seq[m] < t:
            min = m + 1
        elif seq[m] > t:
            max = m - 1
        else:
            return m


class SuperSearch():
    def __init__(self, filename):
        self.keywordsFilename = filename
    def loadKeywords(self):
        words = set(open(self.keywordsFilename, "r").read().split())
        keywords = {}
        for word in words:
            word_distance = _calculate_distance(word)
            keywords.setdefault(word_distance, []).append(word)
        self.keywords = keywords
        self.keys = sorted(list(self.keywords.keys()))
    def search(self, searchKeyword):
        distance = _calculate_distance(searchKeyword)
        id = mbsearch(self.keys, distance)
        return ", ".join(self.keywords[self.keys[id]])

