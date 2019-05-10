from gevent import monkey
monkey.patch_all()
import gevent,time,requests
from gevent.queue import Queue

start=time.time()
url_list=[
    'https://www.baidu.com/',
    'https://www.sina.com.cn/',
    'http://www.sohu.com/',
    'https://www.qq.com/',
    'https://www.163.com/',
    'https://www.iqiyi.com/',
    'https://www.tmall.com/',
    'https://www.ifeng.com/'
]
work=Queue()
for url in url_list:
    work.put_nowait(url)

def crawler():
    while not work.empty():
        url=work.get_nowait()
        res=requests.get(url)
        print(url,work.qsize(),time.time()-start,res.status_code)

task_list=[]
for i in range(2):
    task=gevent.spawn(crawler)
    task_list.append(task)

gevent.joinall(task_list)
end=time.time()
print(end-start)
