import HTMLParser
import html2text
from io import StringIO
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen



#Basic Utility functions
"""
def get_next_target(page):
        start_link=page.find('<a href=')
        if start_link==-1:
                return None,0
        start_quote=page.find('"',start_link)
        end_quote=page.find('"',start_quote+1)
        url=page[start_quote+1:end_quote]
        return url,end_quote

def print_all_links(page):
        while True:
                url, endpos=get_next_target(page)
                if url:
                        print (url)
                        page=page[endpos:]
                else:
                        break
"""



#This function is used to get the content of a page, and would store it in a file of the name same as the url.
def get_page_text(page):
        html=get_page(page)
        if html=="!":
            return 0
        p = html2text.HTML2Text()
        text = p.handle(str(html))
        #use the standard HTML2Text() class to get the raw text from the page.

        raw_list = text.splitlines()
        new_list = []
        #Get the lines within a page
        for line in raw_list:
                line = line.strip()
                line=line.replace('\n','')
                line=line.replace('\t','')
                #replacing useless characters
                if line != '':
                    new_list.append(line)

        clean_text = "\n".join(new_list)
        #get clean text

        if page.find("https://")==-1:
            file_name=page[7:].replace('/','-') #incase the link starts from http://
        else:
            file_name=page[8:].replace('/','-') #incase the link starts from https://
        
        
        f=open(file_name+'.txt',"w")
        f.write(clean_text)
        f.close()
        return 1


def get_page(url):
    try:                                
        return urlopen(url).read()
    except urllib.error.HTTPError as e:
        #An error checking mechanism.
        """
        print (url)
        print ("ERROR GETTING THE PAGE")
        print (e.code)
        print (e.read())
        """
        return "!"

#this function gets all the outlinks connected to a page.
def get_all_links(page):
    links=[]        
    for link in soup.find_all('a'):
        #getting all links
        link=str(link.get('href'))
        #getting the target of these links, which would mostly be links as well
        if link=="#" or link=="/":
            continue

        if link.find("http://")== -1 and link.find("https://") == -1:
            #relative link
            if link[0]=='/':
                link=page+link
            else:
                link=page+'/'+link

            if link[len(link)-1]=='/':
                link = link[:len(link)-1]

            links.append(link)
            #absolute link
        elif link!=page:
            links.append(link)         
    return links

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)
                    

#This function is the primary function used to crawl the website
def crawl_web(seed, pages_to_crawl):
        #start with the seed (homepage) url.
        tocrawl=[seed]
        #the tocrawl array stores the pages that are yet to be crawled.
        crawled=[]
        #the crawled array stores the pages that have already been crawled.
        graph={}
        #the graph is basically a dictionary, with a page pointing to a list of pages it has outlinks to.

        #the while loop must run until either there are no more pages to crawl, or we've reached the limit
        while tocrawl and len(crawled)<pages_to_crawl:
            #open a file to store the URLs that are being crawled.
            f_crawled=open("crawled.txt","a+")
            page=tocrawl[0]
            #this is the page that would be chosen to crawl from.
            
            tocrawl=tocrawl[1:]
            #this page is no longer needed to be crawled.
            if page not in crawled:
                #This condition ensures that the same pages are not being crawled again, avoiding a deadlock
                outlinks=get_all_links(page)
                #outlinks is a list of pages outlinked from this page
                union(tocrawl,outlinks)
                #add the outlinks to the list of webpages that are yet to be crawled.
                graph[page]=outlinks
                #construct the graph
                success = get_page_text(page)
                if success==1:
                    crawled.append(page)
                    #This page has been succesfully crawled.
                    f_crawled.write(page+"\n")
                    #Write the content of the page to the file that we had opened earlier.
                    f_crawled.close()

        return graph


#The website which we chose to search our query in.
page="https://nlp.stanford.edu"
content=get_page(page)
soup=BeautifulSoup(content, features = "lxml")

#Taking input from the user as to the total number of webpages to crawl.
no_pages = int(input("How many pages to crawl?: "))

print("Crawling web pages, please wait....")
graph=crawl_web(page, no_pages)
print("Crawling complete!")

#The below code can be used for printing the graph.
"""
for key, list_of_neighbors in graph.items():
    print(key+ "-->")
    for neighbor in list_of_neighbors:
        print(neighbor+" ")
    print("\n")
"""
