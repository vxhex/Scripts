from mechanize import Browser
from bs4 import BeautifulSoup
import os
import time

br = Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

while True:
    r = br.open('http://pastebin.com/archive')
    soup = BeautifulSoup(r.read())
    a = soup.find('table', {'class' : 'maintable'}).findAll('tr')[1].td.a
    title = a.text
    url = 'http://pastebin.com/raw.php?i=' + a['href'][1:]
    r = br.open(url)

    os.system('clear')
    print title + ' (' + url + ')'
    print '************************************************************************************************************'
    lines = r.read().splitlines()
    for line in lines[:35]:
        print line
    print '************************************************************************************************************'

    time.sleep(30)

