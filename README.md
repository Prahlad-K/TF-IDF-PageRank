# TF-IDF-PageRank
Uses a special score that combines the functionalities of the TF-IDF measure and the PageRank algorithm's ranks to produce improved search results.

Name: K.Prahlad

Class: B.Tech Computer Science 3rd Year, 2nd Semester

Roll Number: 167227

Subject: Advanced Data Mining

This project is part of the course Advanced Data Mining, as required for the minor examination.

Project Aims:

1. To understand the basic working of a general search engine, and to implement TF-IDF and the Google PageRank Algorithm. 
2. To search a given query on a given website, and rank all webpages in terms of a score that uses the TF-IDF of the query keywords with respect to the website corpus and the PageRank obtained from performing Web Mining on the website.

Project inputs/parameters:

1. Maximum number of webpages to crawl in the website.
2. The total number of iterations to update PageRank.
3. The Damping Factor
4. The Query sentence/ string

Project Description:

Most basic search engines have main 3 parts:
1. Crawler
2. Indexer
3. Query Processor

Crawler:
A crawler crawls the web page, fetch the contents and links in the page and stores them. 
The developer of a website can define a file called Robot.txt that defines how frequently a crawler is allowed to crawl and 
which web pages it is allowed to crawl. The crawler program in this project works in a similar fashion, looking up new links exhaustively and storing their content. It also computes the graph (web structure mining) of the webpages, used for PageRank.
 
Indexer:
Creates indices to store each word in the content of every URL. This process helps the calculation of TF-IDF and is also used to analyze and know the pages associated with the keywords in the search query entered.

Query Processor:
This program takes the graph created by the crawler to calculate the PageRank of every document. To calculate  



By default, as an example the official Stanford NLP group website has been taken as the website in which we would search our queries.

