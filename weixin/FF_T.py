

from wxpy import *

bot = Bot(console_qr=True,cache_path=True)

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

     mps = bot.core.search_mps(name="美食天下")
     userName = mps[0]['UserName']
     bot.core.send("3/23.25 品川 14-22 ", toUserName=userName)


# 最终解决了。鉴于时间就每天早上半点左右，清除之前的缓存文件，用xshell先扫码登陆
# 之后把xshell退出，再用手机端登陆即可！无缝连接即可！
# 最新和追加都可以测试一下
if __name__=="__main__":

    try:
        strugglegroup = bot.groups().search('ENTRY - 19群')[0]
        print_group_msg(strugglegroup)

    except:
        pass
    embed()
