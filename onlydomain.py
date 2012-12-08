#!/usr/bin/env python

dom = []
price = []

def get_page(page):
    import urllib2
    source = urllib2.urlopen(page)
    return source.read()

def get_next_item(page, start_atr, end_atr, delim):
    """
    loops for getting next item
    """
    start = page.find(start_atr)
    if start == -1:
        return None, 0
    start_period = page.find(delim, start + 1)
    end_bracket = page.find(end_atr, start_period)
    item = page[start_period:end_bracket]

    return item, end_bracket

def get_all_items(page, start_atr, end_atr, delim, arr):
    x = 0
    #arr = []
    while True:
        item, end = get_next_item(page, start_atr, end_atr, delim)
        
        if item:
            arr.append(item)
            page = page[end:]
        else:
            break

def compile_items(page):
    url = get_page(page)
    get_all_items(url, "tld['product']", "'", '.', dom)
    get_all_items(url, "tld['price']", "'", ".", price)
    #for domain, p in (dom, price):
    #    dic[domain] = p


compile_items('http://www.onlydomains.com/domain-names/domain-pricing')
print dom
print price
