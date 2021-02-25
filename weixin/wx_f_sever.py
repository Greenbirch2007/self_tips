
# 两种改进思路：
# 1.直接使用wxpy，想办法给公众号发信息



# 2. 从头来想办法解决itchat的跟踪问题




# 思路二
# @itchat.msg_register(TEXT, isGroupChat=True)  # 这里的TEXT表示如果有人发送文本消息，那么就会调用下面的方法
# def simple_reply(msg):
#     rooms = itchat.search_chatrooms(name='CUE日本留学生活')  # 找到群名
#     # print(rooms[0]['UserName'])
#     if len(rooms) != 0:
#         message = msg['Content']
#         mps = itchat.search_mps(name="美食天下")
#         print(mps)
#         # 发送方法和上面一样
#         userName = mps[0]['UserName']
#         itchat.send("品川、、", toUserName=userName)
# itchat.auto_login(hotReload=True)  # hotReload = True  不用重复扫描二维码
# itchat.run()
import time

import itchat
from wxpy import *
import datetime

#bot = Bot(console_qr=True) #如果是在服务器不能弹出二维码,可以选择使用这个,可以改True为1,2,3 来改变图案的大小
# bot = Bot(cache_path=True) #开启缓存,不必每次都扫码

#尝试挂在服务器上linux  console_qr 参数
#bot = Bot(console_qr=2, cache_path=True)


# 按照现在服务器的这个脚本就可以，但是在手机上无法完整显示二维码！
# 修改代码和换app已经没有用了。想着如何可以不用扫码！
bot = Bot(console_qr=True,cache_path=True)




#注册后就自动获取信息
@bot.register(Group, TEXT)
def print_group_msg(msg):# 基本可以跟踪群消息，调整之后 捕获字段成功
    str_msg = str(msg)
    print(str_msg)
    # 下面这个判断不怎么有效！？
    if "追加" in str_msg: # 捕获的精确.第一次不算捕获吗？ 直接用
        print("最新+追加成功")

        bot.file_helper.send(msg) # 跟踪测试
        bot.file_helper.send("捕获字段成功") #跟踪测试
        send_MP()

    else:
        print("追加失败")



def send_MP():
    # 还是要使用bot实例化后的登陆
     # mps = itchat.search_mps(name="美食天下")
     mps = bot.core.search_mps(name="美食天下")
     userName = mps[0]['UserName']
     bot.core.send("3/23.25 品川 14-22 ", toUserName=userName)

#使用 itchat 的原接口
# 只需在 wxpy 的 Bot 对象后紧跟 .core.* 即可调用 itchat 的原接口。
#
# 例如，使用 itchat 的 search_friends 接口:
#
# from wxpy import *
# bot = Bot()
# found = bot.core.search_friends('游否')


    #itchat.send("品川信息 捕捉发送测试、", toUserName=userName)



# 问题现在是给公众号发送信息和跟踪群信息不是一个登陆实例
# 所以还要解决两个的和发送的问题！周末消息也不多，所以周中吧！




# 想办法解决LOG OUT的登出问题
#先改进代码吧！
if __name__=="__main__":

    # 1.跟踪微信群，并识别字段(传给文件传输对象，用于测试)

# 开始  跟踪ENTRY - 19群
    try:
        strugglegroup = bot.groups().search('ENTRY - 19群')[0]
        print_group_msg(strugglegroup)

    except:
        pass
    embed()


    # 2.指定公众号，发送指定字段（直接测试即可）

   # 保持登陆 / 运行::

    # 进入 Python 命令行、让程序保持运行


    # 或者仅仅堵塞线程
    # bot.join()
