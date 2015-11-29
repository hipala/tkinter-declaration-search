# -*- coding: utf-8 -*-
import time
import requests
from bs4 import BeautifulSoup

change = [n for n in range(0, 1)]
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36'}
link = "Page={}"  # add link here
sleep = time.sleep(2)

dic = {}


def store(link):

    for n in change:
        new_link = link.format(n)

        target = requests.get(new_link, headers=head)
        target.encoding = "big5"  # notice

        soup = BeautifulSoup(target.text)

        for title in soup.select(".title-sub"):
            dic[title.text] = new_link  # dic = {title:link}

        sleep


store(link)  # execute

# print dic

title = list(dic.keys())  # save titles in key before, turn dic to list
link = list(dic.values())  # save link in value before, turn dic to list
final_results = zip(title, link)  # [(title, link), (title, link)...]

# print final_results
