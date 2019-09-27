import requests,jieba,wordcloud
from bs4 import BeautifulSoup
comments=open('comments.txt','w+',encoding='utf-8')

for i in range(5):#目前只爬取前100条热评，可以增加
    allurl='https://movie.douban.com/subject/27010768/reviews?start='+str(i*20)
    res=requests.get(allurl)
    html=res.text
    soup=BeautifulSoup(html,'html.parser')
    items=soup.find('div',class_="article").find('div',class_="review-list").find_all(class_='main-bd')
    #print(items)
    for item in items:
        comment_url=item.find('a')['href']
        #print(comment_url) #热评列表没有展示每个热评的全文，测试是否拿到热评全文的链接
        res2=requests.get(comment_url)
        html2=res2.text
        soup2=BeautifulSoup(html2,'html.parser')
        items2=soup2.find('div',class_="article").find('div',id="link-report").find_all('p')#热评全文的文字部分，不需要图片和其他非文本信息
        for item2 in items2:
                #print(item2.text) #测试是否拿到纯文本热评内容
                comments.writelines(item2.text)
comments.close()
f=open('comments.txt','r',encoding='UTF-8')
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=' '.join(ls)
w=wordcloud.WordCloud(width=800,height=600,background_color='white',font_path='msyh.ttc',max_words=100)
w.generate(txt)
w.to_file('豆瓣某电影热评.png')
f.close()
