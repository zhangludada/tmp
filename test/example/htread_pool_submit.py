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
    return url

def get_all_url():
    urls=['http://www.dygangs.com/ys/index.htm']
    for i in range(2,13):
        url='http://www.dygangs.com/ys/index_{}.htm'.format(i)
        urls.append(url)
    return urls

def main():
    MAX_WORKS=10
    urls=get_all_url()
    res=[]
    with concurrent.futures.ThreadPoolExecutor(min(MAX_WORKS,len(urls))) as executor:
        for url in urls:
            res.append(executor.submit(parse_html,url))

    for future in concurrent.futures.as_completed(res):
        #future是future对象，future.result()是返回值
        print('{} is {}'.format(future,future.result()))

if __name__ == '__main__':
    main()