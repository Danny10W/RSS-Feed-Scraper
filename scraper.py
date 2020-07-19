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
                #for cleanquestion in cleanedquestions:
                if '+000' in cleanedquestions:
                    pass
                elif '[' in cleanedquestions:
                    pass
                else:
                    print cleanedquestions


                # if '&#8217;' in goodquestion:
                #     #cleangoodquestion = re.finditer(r'(.*)&#8217;(.*)',goodquestion)
                #     #print cleangoodquestion
                #     for cleanedquestion in cleangoodquestion:
                #         cleanedquestion.relace('&#8217;', "'")
                #         #print cleanedquestion.group(1)
                #         #print cleanedquestion.group(2)
                # else:
                #     # if '+000' in goodquestion:
                #     #     pass
                #     # elif '[' in goodquestion:
                #     #     pass
                #     # else:
                #     #     print goodquestion
                #     pass

        except Exception, e:
            print str(e)

    except Exception,e:
        print str(e)
        pass

main()