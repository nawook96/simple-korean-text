# -*- encoding: utf-8 -*-

from konlpy.tag import Kkma
import pymysql.cursors
import operator

ip = 'localhost'
id = 'testuser'
pw = 'AsDf1234!'
db = 'qnaboard'

conn = pymysql.connect(ip,id,pw,db,charset="utf8")

curs = conn.cursor()
sql = "select * from board"

curs.execute(sql)
result=curs.fetchall()
i=0
sen = []

kkma = Kkma()
w_count = {}

for t, c in result:
	s = t + " " + c
	kk = kkma.nouns(s)
	for lst in kk:
		try: w_count[lst] += 1
		except: w_count[lst] = 1

sorted_w = sorted(w_count.items(), key=operator.itemgetter(1))
print(sorted_w)

conn.close()
