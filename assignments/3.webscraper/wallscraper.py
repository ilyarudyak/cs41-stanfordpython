#!/usr/bin/env python3 -tt
"""
File: wallscraper.py
--------------------
Assignment 3: Wallscraper
Course: CS 41
Name: <YOUR NAME>
SUNet: <SUNet ID>

Replace this with a description of the program.
"""
import wallscraperutils
import requests
import urllib.request
import urllib.parse
import os


def queryIntoDic(subreddit):
    '''
    Returns the JSON server response from reddit 
    for provided subreddit as a Python dictionary.
    '''
    # TODO add error handling
    baseUrl = 'https://www.reddit.com/r/'
    urlStr = urllib.parse.urljoin(baseUrl, subreddit + '.json')
    response = requests.get(urlStr, headers={'User-Agent': 'Wallscraper Script by sredmond'})
    return response.json()

def queryIntoListOfPosts(subreddit, score=500):
    # TODO add error handling
    posts = queryIntoDic('wallpapers')['data']['children']
    return [RedditPost(post['data']) for post in posts if post['data']['score'] >= score]

class RedditPost:
    def __init__(self, data):
        self.title = data['title']
        self.score = data['score']
        self.url = data['url']

    def download(self):
        downloadDir = 'wallpapers'
        imgName = self.url.split('/')[-1]
        urllib.request.urlretrieve(self.url, os.path.join(downloadDir, imgName))

    def __str__(self):
        return "{} ({}): {}".format(self.title, self.score, self.url)


def main():
    # test for queryIntoDic(): number of posts with a score greater than 500
    # posts = queryIntoDic('wallpapers')['data']['children']
    # for post in posts:
    #     if post['data']['score'] >= 500:
    #         print(post['data']['title'], ':', post['data']['score']) 

    # test for queryIntoListOfPosts(): number of posts with a score greater than 500
    # posts = queryIntoListOfPosts('wallpapers')
    # for post in posts:
    #         print(post) 

    # download photos from posts with score >= 500
    posts = queryIntoListOfPosts('wallpapers')
    for post in posts:
        post.download()

if __name__ == '__main__':
    main()









