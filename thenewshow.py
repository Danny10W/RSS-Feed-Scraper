import time
import urllib2
from urllib2 import urlopen
import re
import cookielib, urllib2
from cookielib import CookieJar
import datetime

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def main():
    try:
        page = 'https://thenew.show/feed/podcast'
        sourceCode = opener.open(page).read()
        #print sourceCode

        try:
            goodquestions = re.findall(r'\d\d:\d\d:\d\d\s(.*)<',sourceCode)

            for goodquestion in goodquestions:
                cleanedquestions = goodquestion.replace("&#8217;", "")
                if '+000' in cleanedquestions:
                    pass
                elif '[' in cleanedquestions:
                    pass
                else:
                    print cleanedquestions
                    
        except Exception, e:
            print str(e)

    except Exception,e:
        print str(e)
        pass

main()