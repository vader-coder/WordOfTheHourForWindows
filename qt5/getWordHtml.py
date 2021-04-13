from loadHtml import loadFile
from woth_api import WothAPI
woth_data = WothAPI.fetch()
from collections import deque


def head() -> str:
    return loadFile("head.html")

def tail() -> str:
    return loadFile("tail.html")

#maybe once generate it one time, store it and the day and time. on startup, 
#if it is a new day, load it again. store in same html file each time. 
def dailyWordHtml() -> str:
    word = woth_data['word']
    definitions = woth_data['definitions']['english']
    translations = woth_data['translations']
    docHead = head()
    docHead = docHead.replace('equivalent', word)#replace old word with current one
    htmlList = deque([docHead])#add html pieces to list, then join them.
    for definition in definitions:
        htmlList.append('<li class="data">'+definition+'</li>\n')
    htmlList.append('</ol>\n<h3>Translations</h3>\n<ul>\n')
    for language, translation in translations.items():
        htmlList.append('<li><span class="label">'+language+':</span> '+translation+'</li>\n')
    htmlList.append('</ul>\n')
    htmlList.append(tail())
    return ''.join(htmlList)
