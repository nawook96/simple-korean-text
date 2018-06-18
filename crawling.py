import os,sys
import requests
from bs4 import BeautifulSoup
import pymysql

mid = 'qna'

ip = 'localhost'
id = 'admin'
pw = 'As3515954!'
name = 'qnaboard'
chs = 'utf8'

conn = pymysql.connect(ip,id,pw,name,charset="utf8")

curs = conn.cursor()
sql = "insert into board(title,content) value (%s, %s)"

url = 'http://board.namu.wiki/index.php'
for i in range(100,101):
    params = {
            'mid':mid,
            'page':i
            }
    r = requests.get(url, params)

    soup = BeautifulSoup(r.content, "html.parser")
    r.close()


    for board in soup.find_all('tr', attrs={'class':None}):
        board2 = board.find('td',attrs={'class':'title'})
        url = board2.a["href"]
        title = board2.find("a")
        title = title.get_text()
        print(title)
        r=requests.get(url)
        soup2 = BeautifulSoup(r.content, "html.parser")
        cont = soup2.find("div", attrs={'class':'read_body'})
        content=''
        for cont2 in cont.find_all('p'):
            content = content + cont2.get_text()
        print(content)
        print("########################")
        curs.execute(sql,(title,content))
        conn.commit()





