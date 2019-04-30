import math


#Here 2 indices are constructed- one used while calculating pagerank, and one for TF-IDF. 
def make_indices():
        word_to_urls={}
        url_to_words = {}
        f_crawled=open("crawled.txt","r")
        #contains the list of URLs we have crawled.
        for line in f_crawled.readlines():
                line=line.replace('\n','')
                url=line
                if line.find("https://")==-1:
                        line = line[7:] #incase the link starts from http://
                else:
                        line = line[8:] #incase the link starts from https://

                line=line.replace('/','-')
                line=line+'.txt'
                f_file=open(line,"r")
                content=f_file.read()
                #opening the file in which the content of the webpage would be found.

                words=content.split()
                for word in words:
                        add_to_word_to_urls(word_to_urls,word,url)
                        add_to_url_to_words(url_to_words,word,url)

        return word_to_urls, url_to_words


def add_to_word_to_urls(word_to_urls,keyword,url):
        if keyword in word_to_urls:
                if url not in word_to_urls[keyword]:
                        word_to_urls[keyword].append(url)
        else:
                word_to_urls[keyword]=[url]   

def add_to_url_to_words(url_to_words, keyword, url):
        if url in url_to_words:
                url_to_words[url].append(keyword)
        else:
                url_to_words[url] = [keyword]


word_to_urls, url_to_words = make_indices()

print("Indexing of all the words of each link in the website complete!")



