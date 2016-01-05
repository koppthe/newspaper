# coding: utf-8

"""
下载需要的 NLTK 模块和语料库
"""

import nltk

REQUIRED_CORPORA = [
    'brown',  # FastNPExtractor
    'punkt',  # WordTokenizer
    'maxent_treebank_pos_tagger',  # NLTKTagger
    'movie_reviews',  # NaiveBayesAnalyzer
    'wordnet',  # Lemmatization and Wordnet
    'stopwords'
]

def main():
    for each in REQUIRED_CORPORA:
        print(('Downloading "{0}"'.format(each)))
        nltk.download(each)
    print "Finished."

if __name__ == '__main__':
    main()
