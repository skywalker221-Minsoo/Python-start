import pymysql

def create(id, pw, name, tel):
    con = pymysql.connect(host='localhost', user='root', password='1234',
                          port=3306, db='shop')
    print(con)

    curs = con.cursor()
    print(curs)

    sql = 'insert into member values ("' + id + '", "' + pw + '","' + name + '","' + tel + '")'
    result = curs.execute(sql)
    print(result)

    con.commit()
    con.close()

def delete(id):
    con = pymysql.connect(host='localhost', user='root', password='1234',
                          port=3306, db='shop')

    curs = con.cursor()

    sql = 'delete from member where id = ("'+id+'")'
    curs.execute(sql)

    con.commit()
    con.close()

def create2(data):
    con = pymysql.connect(host='localhost', user='root', password='1234',
                          port=3306, db='shop')
    print(con)

    curs = con.cursor()
    print(curs)

    #작은따옴표 3개면 엔터 눌러도 sql문은 유효하다!
    sql = '''insert into member values
    (%s, %s, %s, %s)'''
    result = curs.execute(sql, data)
    print('처리 결과 :', result, '개')

    con.commit()
    con.close()

def update(id, tel):
    con = pymysql.connect(host='localhost', user='root', password='1234',
                          port=3306, db='shop')
    print(con.get_host_info())

    #2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득!
    cur = con.cursor()
    print(cur)

    #3. sql문을 만들어서 전송함.
    data = (tel, id)
    sql = 'update member set tel = %s where id = %s'
    cur.executemany(sql, data) #tuple로 넣어준다.

    #4. auto-commit이 안된다. 수동으로 반영시켜야 한다.
    con.commit()
    con.close()

def create3(datas):
    con = pymysql.connect(host='localhost', user='root', password='1234',
                          port=3306, db='shop')
    print(con.get_host_info())

    curs = con.cursor()
    print(curs)

    #작은따옴표 3개면 엔터 눌러도 sql문은 유효하다!
    sql = '''insert into member values
    (%s, %s, %s, %s)'''
    result = curs.executemany(sql, datas)
    print('처리 결과 :', result, '개')

    con.commit()
    con.close()

def read():
    con = pymysql.connect(host='localhost', user='root', password='1234',
                          port=3306, db='shop')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    # 작은따옴표 3개면 엔터 눌러도 sql문은 유효하다!
    sql = "select * from member where id = 'apple'"
    cur.execute(sql)

    row = cur.fetchone()
    # cur.fetchall() : 조건에 맞는 목록을 모두 가지고 온다.
    # cur.fetchmany(개수) : 조건에 맞는 목록을 개수만큼 가지고 온다.
    print(row)

    con.close()

def read2():
    con = pymysql.connect(host='localhost', user='root', password='1234',
                          port=3306, db='shop')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    # 작은따옴표 3개면 엔터 눌러도 sql문은 유효하다!
    sql = "select * from member where id = 'apple'"
    cur.execute(sql)

    row = cur.fetchmany(5)
    # 조건에 맞는 목록을 개수만큼 가지고 온다.
    print(row)
    print(row[0])
    print(type(row))

    con.close()

def read3():
    con = pymysql.connect(host='localhost', user='root', password='1234',
                          port=3306, db='shop')
    print(con.get_host_info())

    cur = con.cursor(pymysql.cursors.DictCursor)
    print(cur)

    # 작은따옴표 3개면 엔터 눌러도 sql문은 유효하다!
    sql = "select * from member"
    cur.execute(sql)

    rows = cur.fetchall()
    # cur.fetchmany(개수) : 조건에 맞는 목록을 개수만큼 가지고 온다.
    print(rows)
    # print(rows[0])
    print(type(rows))
    for row in rows:
        print(row)

    con.close()