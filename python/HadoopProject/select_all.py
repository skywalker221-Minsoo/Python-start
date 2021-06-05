import pymysql
import matplotlib.pyplot as plt

def select_all():
    conn = pymysql.connect(
        user='root',
        passwd='1234',
        host='localhost',
        port=3306,
        db='hadoop',
        charset='utf8'
    )
    #print(conn.user)
    #cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    sql = "select * from counttable where countid >= 100 order by countid DESC limit 10"
    cursor.execute(sql, ) #파라미터가 있을 수 있으므로
    conn.commit()

    result = cursor.fetchall()
    print(result)
    name = list()
    countid = list()
    for x, y in result:
        print(x, y)
        name.append(x)
        countid.append(y)
    print(name)
    print(countid)

    plt.figure()
    plt.pie(countid, labels=name)
    plt.show()

if __name__ == '__main__':
    select_all()



