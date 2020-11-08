#!/bin/env python3

import re
import requests


#fileter urls 
def url1(bundle):
    ex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(ex,bundle)
    return [x[0] for x in url]
##writng files to output
def wr():
        writ = open("boom.txt","a")
        writ.write(test())
        writ.close()

##funtion to pop array to store nul variable 
def test():
    for multi1 in url1(boom):
        print(multi1 + "\n") 
                #w = open("links.txt","a")
                #w.write(mul)
                #w.close()

##main funtions call input place
if __name__ == '__main__':
        boom = requests.get("https://hkcybersolutions.com/").text
        test()
