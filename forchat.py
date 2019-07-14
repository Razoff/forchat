#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from random import randint
from bs4 import BeautifulSoup # For scraping html

def getUrl():
    max_num = getMaxQuoteNum()

    if max_num < 0:
        print("Error while retrieving last quote number")
        exit(max_num)

    return "https://danstonchat.com/" + str(randint(1, max_num)) + ".html"

def getQuote(url):
    try: 
        page = urlopen(getUrl())
    except:
        return "Error while loading DTC url"

    try:
        soup = BeautifulSoup(page, 'html.parser')
        start_quote = soup.find_all('span', attrs={'class': 'decoration'}) # Pseudo of the quote all have the class decoration

        ret = ""
        for i in range(len(start_quote)):
            ret += (start_quote[i].contents[0] + str(start_quote[i].next_sibling) + "\n") # Each quote line is the pseudo + the next neighbourg (text)

        return ret
    except:
        return "Error while parsing quote"

def getMaxQuoteNum():
    try:
        page = urlopen("https://danstonchat.com")
    except:
        return -1

    try:
        soup = BeautifulSoup(page, 'html.parser')
        h3_tag_content = str(soup.find('h3')) # there is an <a> in the only h3 where the max number can be found in the href
    except:
        return -2

    try:
        max_num = h3_tag_content.split("\"")[1].replace('/','.').split(".")[-2] # 1) get the href="url" part 2) get the number in url 
    except:
        return -3

    return int(max_num)

def main():
    print(getQuote(getUrl())) # Print in terminal

if __name__ == "__main__":
    main()
