import json
import requests
from bs4 import BeautifulSoup

def main():
    r = requests.get('http://revistaautoesporte.globo.com/rss/ultimas/feed.xml')
    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.find_all('item')
    items2 = []
    for it in items:
        descr = it.description.contents[0]
        soup2 = BeautifulSoup(descr, 'html.parser')
        item = {
            'descr': []
        }
        item['title'] = it.title.text
        item['link'] = it.link.next_sibling.strip('\n').strip()
        for content in soup2.contents:
            if content.name == 'p':
                #print(content.text)
                if content.text.strip():
                    item['descr'] += {
                        'type': 'text',
                        'content': content.text.strip('\r\n').strip('\t').strip('\n')
                    },
            elif content.name == 'div':
                if content.img:
                    item['descr'] += {
                        'type': 'image',
                        'content': content.img['src']
                    },
                    #print(content.img['src'])
                elif content.ul:
                    links = []
                    for li in content.ul.contents:
                        if li.name == 'li':
                            links += li.a['href'],
                    #print(links)
                    item['descr'] += {
                        'type': 'links',
                        'content': links
                    },
        items2 += item,
    #print(json.dumps(item))
    return items2
    