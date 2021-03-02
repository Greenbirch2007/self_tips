import pymysql

def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JP_ENTRY',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()

    try:

        cursor.executemany('insert into JP_jobENTRY (Dcontent) values (%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError:
        print("插入数据库失败~")


s_str = "ENTRY - 19群 › ㈱エントリー : ❤ ❤本日最新更新❤ ❤ ↩ 3/4 （周四） ↩ 東京モノレール　流通センター駅 14-18 仓库检品 时给1339 N2男生 (Text)"


f_msg = [(s_str)]
insertDB(f_msg)
