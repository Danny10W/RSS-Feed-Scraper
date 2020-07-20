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
        page = 'https://feeds.fireside.fm/usererror/rss'
        sourceCode = opener.open(page).read()
        #print sourceCode

        try:
            goodquestions = re.findall(r'\d\d:\d\d:\d\d\s(.*)<',sourceCode)
            for goodquestion in goodquestions:
                cleanedquestions = goodquestion.replace("&#8217;", "")
                dblcleanedquestions = cleanedquestions.replace("&#39;", "")
                if '+000' in dblcleanedquestions:
                    pass
                elif '[' in dblcleanedquestions:
                    pass
                elif '-\d' in dblcleanedquestions:
                    pass
                elif re.search(r'-\d', dblcleanedquestions):
                    pass
                elif re.search('&quot;', dblcleanedquestions):
                    doublecleanlines = dblcleanedquestions.replace("&quot;", "\"")
                    print doublecleanlines
                else:
                    print dblcleanedquestions
                    #sort <file name> | uniq
                    
        except Exception, e:
            print str(e)

    except Exception,e:
        print str(e)
        pass

main()