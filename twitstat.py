# https://dev.twitter.com/docs/api/1/get/statuses/user_timeline
#
# Alt url: http://api.twitter.com/1/statuses/user_timeline/vxhex.xml?include_rts=true&count=5 

import urllib.request
import xml.dom.minidom
import string

username = "TwitterHandle"
retweets = "true"
count = "200"
verbose = True
target = "Keyword"

url = "https://api.twitter.com/1/statuses/user_timeline.xml"
url = url + "?screen_name=" + username
url = url + "&include_rts=" + retweets
url = url + "&count=" + count

with urllib.request.urlopen(url) as feed:
    xmlfeed = feed.read()

elements = xml.dom.minidom.parseString(xmlfeed)
statii = elements.getElementsByTagName("status")

tweetCountTotal = 0
tweetCountContaining = 0

for status in statii:
    tweetCountTotal += 1
    text = status.getElementsByTagName("text")[0].firstChild.data
    if target.upper() in text.upper():
        tweetCountContaining += 1
    if verbose:
        print("***TWEET("+ username +"): " + text)

print("\n***OUTPUT***")
print("URL used: " + url)
print("Requested " + count + " tweets from " + username + ".")
print("Read " + str(tweetCountTotal) + " tweets in total.")
print(str(tweetCountContaining) + " tweets contained '" + target + "'.")
percentage = (tweetCountContaining / tweetCountTotal) * 100
print("Target / Total = %" + str(percentage))
