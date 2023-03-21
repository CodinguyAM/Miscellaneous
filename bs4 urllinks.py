import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import socket

# Ignore SSL certificate errors
def findLinks(url):
    if url[-1] != "/":
        url = url + "/"
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    linkedTo = []
    for tag in tags:
        lurl = tag.get("href", "")
        #print(lurl)
        if len(lurl)>3:
            if lurl[:4] == "http":
                linkedTo.append(lurl)
            elif lurl[0] != "#":
                if lurl[0] != "/":
                    linkedTo.append(url + lurl)
                else:
                    linkedTo.append(url + lurl[1:])
##    for l in linkedTo:
##        print(l)
    return linkedTo
    

def extensibleFL(urls):
    r = []
    for url in urls:
        #print(url)
        try:
            r = r + findLinks(url)
        except urllib.error.HTTPError:
            #print("URLLib HTTPError on, ", url)
            print()
        except socket.gaierror:
            print("Socket GAIError on, ", url)
            
    r = list(set(r))
    return r

efl = extensibleFL

def findWithin(url, md=3):
    r = []
    for d in range(1, md + 1):
        r = r + eval("efl("*d + "['" + url + "']" + ")"*d)
        r = list(set(r))
    return r
fw = findWithin

url = input("URL?: ")
d = int(input("Distance?: "))
twoAway = fw(url, d)
for l in twoAway:
    print(l)
