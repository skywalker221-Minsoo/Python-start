import pymysql

def create(data):
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')

    cur = con.cursor()

    sql = 'insert into bbs values (%s, %s, %s, %s)'
    result = cur.execute(sql, data)

    con.commit()
    con.close()

def read():
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')

    cur = con.cursor()

    sql = 'select * from bbs'
    cur.execute(sql)

    rows = cur.fetchall()
    for row in rows:
        print(row)

def update(bbsid, writer):
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')

    cur = con.cursor()

    data = (writer, bbsid)
    sql = 'update bbs set writer = %s where bbsid = %s'
    result = cur.execute(sql, data)

    con.commit()
    con.close()

def delete(bbsid):
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')

    cur = con.cursor()

    sql = 'delete from bbs where bbsid = "'+bbsid+'"'
    cur.execute(sql)

    con.commit()
    con.close()