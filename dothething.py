#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import argparse

def main():
    r = requests.get(args.url)
    soup = BeautifulSoup(r.content, features="lxml")

    title = soup.title.string
    print ('TITLE IS :', title)

    meta = soup.find_all('meta')

    for tag in meta:
        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords']:
            # print ('NAME    :',tag.attrs['name'].lower())
            print ('CONTENT :',tag.attrs['content'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', dest='url', type=str, help='The URL to be analysed')
    args = parser.parse_args()
    main()