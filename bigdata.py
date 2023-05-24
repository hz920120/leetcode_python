from textblob import TextBlob
corpus = '''The housekeeping service was HORRIBLE The halls were very noisy as
well.
'''
blob_object = TextBlob(corpus)
# Word tokenization of the sample corpus
corpus_words = blob_object.words
# To see all tokens
print(corpus_words)
# To count the number of tokens
print(len(corpus_words))
