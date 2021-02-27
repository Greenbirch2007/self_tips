import pymysql
from wxpy import *

bot = Bot(console_qr=True,cache_path=True)

@bot.register(Group, TEXT)
def print_group_msg(msg):# 基本可以跟踪群消息，调整之后 捕获字段成功
    str_msg = str(msg)
    print(str_msg)
    # 下面这个判断不怎么有效！？
    if  "品川" in str_msg: # 捕获的精确.第一次不算捕获吗？ 直接用
        print("直接测试品川信息")

        bot.file_helper.send(msg) # 跟踪测试
        bot.file_helper.send("捕获字段成功") #跟踪测试
        send_MP()
 
    # elif  "追加" in str_msg: # 捕获的精确.第一次不算捕获吗？ 直接用
    #     print("最新+追加成功")
    # 
    #     bot.file_helper.send(msg) # 跟踪测试
    #     bot.file_helper.send("捕获字段成功") #跟踪测试
    #     send_MP()

    else:
        print("追加失败")
    if "最新" in str_msg:  # 捕获的精确.第一次不算捕获吗？ 直接用
        print("直接测试品川信息")

        bot.file_helper.send(msg)  # 跟踪测试
        bot.file_helper.send("捕获历史字段-- 最新--  成功")  # 跟踪测试
        # 往数据库中插入数据
        f_content=[tuple(msg)]
        insertDB(f_content)

    elif  "追加" in str_msg: # 捕获的精确.第一次不算捕获吗？ 直接用
        print("最新+追加成功")

        bot.file_helper.send(msg) # 跟踪测试
        bot.file_helper.send("捕获历史字段-- 追加--  成功") #跟踪测试
        # 往数据库中插入数据
        f_content=[tuple(msg)]
        insertDB(f_content)

def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JP_ENTRY',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()

    try:

        cursor.executemany('insert into JP_jobENTRY (Dcontent) values (%s)', content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError:
        pass


def send_MP():

     mps = bot.core.search_mps(name="美食天下")
     userName = mps[0]['UserName']
     bot.core.send("3/23.25 品川 14-22 ", toUserName=userName)


# 最终解决了。鉴于时间就每天早上半点左右，清除之前的缓存文件，用xshell先扫码登陆
# 之后把xshell退出，再用手机端登陆即可！无缝连接即可！
# 最新和追加都可以测试一下
# 初步测试效果还是有的，直接上品川测试，多册几次。随意一些
# 2021.2.28  跟踪历史文本信息，便于做统计分析
if __name__=="__main__":

    try:
        strugglegroup = bot.groups().search('ENTRY - 19群')[0]
        print_group_msg(strugglegroup)

    except:
        pass
    embed()



# create table JP_jobENTRY(id int not null primary key auto_increment, Dcontent text,  LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ) engine=InnoDB  charset=utf8;
#
#