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


s_str ="  本日最新更新 3/11.12 各線　品川駅 14-22 （yamato快递检品） 时给1272 无日语要求※上车前请看好巴士是否是レールゲート行き。一定不要做错巴士※　"

f_msg = [(s_str)]
insertDB(f_msg)
