from BeautifulSoup import BeautifulStoneSoup

hard_stuff = u"Hallo \U0001f5fc"

ascii = hard_stuff.encode('ascii','xmlcharrefreplace')
print ascii
easy_stuff = decodedString=unicode(BeautifulStoneSoup(ascii,convertEntities=BeautifulStoneSoup.HTML_ENTITIES ))
print easy_stuff
