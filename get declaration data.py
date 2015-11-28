# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

change = [n for n in range(0, 1)]
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36'}
link = "Page={}"  # add link here
sleep = time.sleep(2)


def store(link):

    page = 0
    for n in change:
        page += 1
        new_link = link.format(n)

        target = requests.get(new_link, headers=head)
        target.encoding = "big5"  # notice

        soup = BeautifulSoup(target.text)

        titles = []
        for title in soup.select(".title-sub"):
            titles.append(title.text)

        times = []
        for time in soup.select(".title-time"):
            times.append(time.text)

        results = []
        for title, time in zip(titles, times):
            results.append(title + ', ' + time + ', ' + new_link)

        for result in results:
            print result

        sleep
