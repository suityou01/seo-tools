#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import argparse

def main():
    
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0'}
    r = requests.get(args.url, headers=headers)
    soup = BeautifulSoup(r.content, features="lxml")

    title = soup.title.string
    print ('TITLE IS :', title)

    meta = soup.find_all('meta')
    print(meta)
    for tag in meta:
        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords']:
            # print ('NAME    :',tag.attrs['name'].lower())
            print ('CONTENT :',tag.attrs['content'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', dest='url', type=str, help='The URL to be analysed')
    args = parser.parse_args()
    main()