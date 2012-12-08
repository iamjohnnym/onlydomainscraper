#!/usr/bin/env python

from itertools import izip

dom = []
comp = []

def get_page(page):
    import urllib2
    source = urllib2.urlopen(page)
    return source.read()

def get_next_item(page, start_atr, end_atr, delim, space):
    """
    loops for getting next item
    """
    start = page.find(start_atr)
    if start == -1:
        return None, 0
    start_period = page.find(delim, start)
    end_bracket = page.find(end_atr, start_period)
    item = page[start_period + space:end_bracket]

    return item, end_bracket

def get_all_items(page, start_atr, end_atr, delim, arr, space):
    x = 0
    #arr = []
    while True:
        item, end = get_next_item(page, start_atr, end_atr, delim, space)
        
        if item:
            arr.append(item)
            page = page[end:]
        else:
            break

def check(pattern, string):
    import re
    
    if re.search(pattern, string):
        return 'false'
    else:
        return "na"

print check('[^\.[0-9][0-9]]','$8.99')
print check('\.[a-z\.]{2,7}', '.com.au')

def compile_items(page):
    url = get_page(page)
    get_all_items(url, "<td", "</td>", ">", dom, 1)
    ugly = '<div style="width:40px;overflow:hidden;">'
    ugly2 = 'For pricing <a href="mailto:info@101domains.com?subject=101Domains'


    x = 1
    y = 3
    z = 4
    inc = 6

    while z < len(dom):
        z += inc
        y += inc
        x += inc

compile_items('http://www.101domains.com/prices.shtml')

#print comp
