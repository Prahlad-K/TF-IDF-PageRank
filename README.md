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

Project Description:

	Most basic search engines have 3 parts:

	1. Indexer
	2. Crawler
	3. Query Processor

	Crawler:

	A crawler crawls the web page, fetch the contens and links in the page and stores them. 
	The developer of a website can define a file called Robot.txt that defines how frequently a crawler is allowed to crawl and 
	which web pages it is allowed to crawl.

	Indexer:

	Indexes the content of web page fetched by crawler. It also filters important words to be indexed out of the content.

	Query Processor

	This program basically processes the query entered by the user, fetches the indexes of the query, calculate the page rank, sort 	them and ten displays the result. This is just simple explanantion of query processor but it includes a lot more than this like 	making sense of the query and give suggestions by using Machine Learning algorrithms.

	All these 3 programs are almost same in each search engine whether it is Microsoft Bing or yahoo or google search engine. They 		all differ in their implementation of Ranking algorithm. Page Rank algorithm is google's patented algorithm.
