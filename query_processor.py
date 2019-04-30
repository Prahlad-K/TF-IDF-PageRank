from crawler import graph #the graph is taken from the crawler.
from indexer import url_to_words, word_to_urls #the two indices we'd calculated during the indexing.
import math

def lookup(word_to_urls,keyword):
        if keyword in word_to_urls:
            return word_to_urls[keyword]
        else:
            return None

def displayPageranks(word_to_urls,ranks,keyword):
	pages=lookup(word_to_urls,keyword)
	for i in pages:
		print(i+" --> ", end = "") 
		print(ranks[i])
	pages_sorted = quickSort(pages,ranks)
	print ("\nAfter Sorting the results by page rank\n")
	for i in pages_sorted:
		print(i) 

def quickSort(pages,ranks):
	if len(pages)>1:
		piv=ranks[pages[0]]
		i=1
		j=1
		for j in range(1,len(pages)):
			if ranks[pages[j]]>piv:
				pages[i],pages[j]=pages[j],pages[i]
				i+=1
		pages[i-1],pages[0]=pages[0],pages[i-1]
		QuickSort(pages[1:i],ranks)
		QuickSort(pages[i+1:len(pages)],ranks)
		return pages

#Implementation of the PageRank equations - the calculation of the pagerank would now take numloops iterations with damping_factor 
def computeRanks(graph, numloops, damping_factor):
	d=damping_factor
	ranks={}
	npages=len(graph)
	for page in graph:
		ranks[page]=1.0/npages

	for i in range(0,numloops):
		newranks={}
		for page in graph:
			newrank=(1-d)/npages
			for node in graph:
				if page in graph[node]:
					newrank=newrank+d*ranks[node]/len(graph[node])
			newranks[page]=newrank
		ranks=newranks
	return ranks

#Computes the term frequency of a document = (frequency of word in document/total number of words in document)
def computeTF(main_word, doc):
        tf =0
        list_of_words = []
        list_of_words = url_to_words[doc]
        for word in list_of_words:
                if word==main_word:
                        tf = tf +1
        tf = tf/len(list_of_words)
        return tf


def computeTFs(word):
        tfs = {}
        for doc in url_to_words:
                tfs[doc] = computeTF(word, doc)

        return tfs

#computes the inverse document frequency of a word = log(total number of documents/number of documents having this word)
def computeIDF(word):
        total_docs = len(url_to_words)
        #print(total_docs)
        num_docs_having_term = 0
        for doc, list_of_words in url_to_words.items():
                if word in list_of_words:
                        num_docs_having_term = num_docs_having_term+ 1
        if num_docs_having_term !=0:
                idf = math.log(total_docs/num_docs_having_term)
        else:
                idf = 0
        return idf

#integrates TFIDF and PageRank to produce a new score- TFIDFPageRank
def calculateTFIDFPagerank(keyword_to_tfidfs, ranks):

	page_to_score = {}
	for page in url_to_words:
		#for every page we had crawled and indexed, 
		sum_tfidf =0
		#initialize the sum of the TF-IDF scores of the keywords that were present in this page
		for keyword, tfidfs in keyword_to_tfidfs.items():
			tfidf = tfidfs[page]# if the page did not have this keyword, it would simply be set to 0
			sum_tfidf = sum_tfidf + tfidf
		#calculating the sum of TF-IDFs			

		#sometimes the sum_tfidf may be zero (if the keyword is present in all documents)
		#in that case, we would get a 0 for this score if we directly multiply!
		#that's why sum_tfidf was added by 1 and then multiplied with the rank of the page.
		page_to_score[page] = (sum_tfidf+1) * ranks[page]

	return page_to_score


#while loop used for experimentation
while(1):
	no_of_iterations = int(input("Enter number of iterations: "))
	damping_factor = float(input("Enter damping_factor: "))
	ranks=computeRanks(graph, no_of_iterations, damping_factor)
	#computing the pageranks

	search_sentence = input("Enter your query: ")
	#takes the input query
	keywords = search_sentence.split()
	#splits it into words
	keyword_to_tfidfs = {}
	#computes the tf-idf scores of the keyword for all documents.
	for keyword in keywords:
		tfs = computeTFs(keyword)
		idf = computeIDF(keyword)
		tfidfs = {}
		for doc, tf in tfs.items():
			tfidfs[doc] = tf * idf
		keyword_to_tfidfs[keyword] = tfidfs

	score = calculateTFIDFPagerank(keyword_to_tfidfs, ranks)
	#calculates the TFIDFPagerank score, which is a dictionary that maps from the page to the score

	final_result = sorted(score.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)
	#sorts the results in a descending order of TFIDFPagerank score.
	print("<-------------------------------------------------->")
	print("Final TF-IDF PageRank score results:")
	rank = 1
	for url, sc in final_result:
		print(rank, end = "")
		print(" : "+ url + " ---> ", end = "")
		print(sc)
		rank = rank + 1
	print("<--------------------------------------------------->")

	#The below call can be used to just print pages ONLY according to their pagerank:-
	#displayPageranks(index,ranks,search_keyword)

