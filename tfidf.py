import math

index = {}
def computeIndex(docs):
	for doc in docs:
		index[doc] = []
		f_file=open(doc,"r")
		for line in f_file:
			words = []
			words = line.split()
			for word in words:
					index[doc].append(word)

def computeTF(main_word, doc):
	tf =0
	list_of_words = []
	list_of_words = index[doc]
	for word in list_of_words:
		if word==main_word:
			tf = tf +1
	tf = tf/len(list_of_words)
	return tf


def computeTFs(word):
	
	tfs = {}
	for doc in index:
		tfs[doc] = computeTF(word, doc)

	return tfs

def computeIDF(word):

	total_docs = len(index)
	print(total_docs)
	num_docs_having_term = 0
	for doc, list_of_words in index.items():
		if word in list_of_words:
			num_docs_having_term = num_docs_having_term+ 1
	if num_docs_having_term !=0:
		idf = math.log(total_docs/num_docs_having_term)
	else:
		idf = 0
	return idf

docs = ['F1.txt', 'F2.txt']

computeIndex(docs)
print(index)

while(1):
	input_word = input("Enter a word for its TFIDF:")

	tfs = computeTFs(input_word)
	idf = computeIDF(input_word)
	print(idf)

	tfidfs = {}
	for doc, tf in tfs.items():
		tfidfs[doc] = tf * idf

	print(tfidfs)

