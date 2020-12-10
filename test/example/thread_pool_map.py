import requests
import concurrent.futures
from pyquery import PyQuery as pq

def parse_html(url):
    r=requests.get(url)
    r.encoding=r.apparent_encoding
    doc=pq(r.text)
    imgs=doc.find('img')
    for img in imgs.items():
        if img.attr('src') and img.attr('alt'):
            name=img.attr('alt')+'.jpg'
            url2=img.attr('src')
            content=requests.get(url2).content
            with open('movies/'+name,mode='wb') as f:
                f.write(content)
            print(name+'写入完成')
    print(url+'全部完成')

def get_all_url():
    urls=['http://www.dygangs.com/ys/index.htm']
    for i in range(2,528):
        url='http://www.dygangs.com/ys/index_{}.htm'.format(i)
        urls.append(url)
    return urls

def main():
    MAX_WORKS=10
    urls=get_all_url()
    with concurrent.futures.ThreadPoolExecutor(min(MAX_WORKS,len(urls))) as executor:
        res=executor.map(parse_html,urls)
        #res是map对象，list是实际返回值
        print(list(res))

if __name__ == '__main__':
    main()