import asyncio
import requests
from pyquery import PyQuery

async def parse_html(url):
    r=requests.get(url)
    r.encoding=r.apparent_encoding
    doc=pq(r.text)
    imgs=doc.find('img')
    for img in imgs.items():
        if img.attr('src') and img.attr('alt'):
            name=img.attr('alt')+'.jpg'
            url=img.attr('src')
            content=requests.get(url).content
            with open('movies/'+name,mode='wb') as f:
                f.write(content)
            print(name+'写入完成')

