from mechanize import Browser
from bs4 import BeautifulSoup
import os
import time

screen_width = 80

br = Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)')]

while True:
    r = br.open('http://pastebin.com/archive')
    soup = BeautifulSoup(r.read())
    rows = soup.find('table', {'class' : 'maintable'}).findAll('tr')[1:6]
    for row in rows:
        a = row.td.a
        title = a.text
        url = 'http://pastebin.com/raw.php?i=' + a['href'][1:]

        os.system('clear')
        print title + ' (' + url + ')'
        print '*' * screen_width
        lines = br.open(url).read().splitlines()
        for line in lines[:35]:
            print line
        print '*' * screen_width

        time.sleep(12)

