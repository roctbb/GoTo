import random
import string
import sqlite3

def getKey(N):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

conn = sqlite3.connect('tanks.sqlite')
c = conn.cursor()

names = ['Revenko Dasha', 'Savlaev Ruslan','Анисимов Мануэль', 'Богомолов Алексей', 'Бондарев Иван', 'Вайсберг Гриша','Волох Андрей','Гийар Филипп','Курылев Александр', 'Павлов Артём', 'Павлов Лев', 'Семкин Владислав', '	Турубанова Светлана', 'Ульяненков Ярослав', '	Черемисина Настя', 'Швецова  Мария']
for name in names:
    key = getKey(8)
    c.execute("INSERT INTO players (name, key, state) VALUES (?,?,?)", [name, key, "waiting"])

conn.commit();

