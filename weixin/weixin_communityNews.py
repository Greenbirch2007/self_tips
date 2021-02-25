

#
# from wxpy import *
#
# bot =Bot()
#
# # 初始化机器人，电脑弹出二维码，用手机微信扫码登陆
#
# bot.groups(update=True,contact_only=False)
#
# #微信登陆后，更新微信群列表（包括未保存到通讯录的群）
#
# my_groups = bot.groups().search("雷苏日语课交流3群")
# bot.file_helper.send("helllll")
# #找出名字包括“铲屎官”的群。假设我们有2个微信群，分别叫“铲屎官1群”、“铲屎官2群”。如果有3个或以上的铲屎群，上面这句代码也能全部找出来，并在后面的代码中实现多群同步。
#
#
# my_groups[0].update_group(members_details=True)
# my_groups[1].update_group(members_details=True)
#
# #注册消息响应事件，一旦收到铲屎群的消息，就执行下面的代码同步消息。机器人自己在群里发布的信息也进行同步。
# @bot.register(my_groups,except_self=False)
# def sync_my_groups(msg):
#     sync_message_in_groups(msg,my_groups)
#     # 同步“铲屎官1群”和“铲屎官2群”的消息。包括文字、图片、视频、语音、文件、分享、普通表情、地图等。
#
# bot.join()
# #堵塞线程，让机器人保持运行
#
# # 个性化：
# #
# # 我们可以根据具体情境优化代码，以满足个性化要求：
# #
# # 1、在Linux服务器运行机器人，需要使用终端二维码。初始化机器人的代码改为：
#
# #console_qr=2，这个整数可以调整。如果终端底色是白色，则改为负数。
# bot= Bot(cache_path=True,console_qr=2)
#
# #2、如果需要同步的群名字不同，可以用以下命令进行指定：
# #指定同步“铲屎官群”和“吃货群”的消息
#
# my_groups[0] = bot.groups.search("铲屎官群")
# my_groups[1] = bot.groups.search("吃货群")
#
# # 3、wxpy在同步群消息时，会默认给发消息的群成员添加一个小图标作为临时头像。如果想使用更简洁的方式，可以改用以下代码：
#
# #给转发的消息加上前缀，显示群成员名字和冒号。群成员名字从备注、群昵称、微信昵称里面按顺序自动获取。
#
# @bot.register(my_groups,except_self=False)
# def sync_my_groups(msg):
#     my_name= msg.member.name+':'
#     sync_message_in_groups(msg,my_groups,prefix=)
#
#
# # 4、在最后增加一条代码，给机器人发送消息，表示代码执行成功
#
# #机器人的文件传输助手发送消息“Hello”
# bot.file_helper.send("helllll")
# bot.join()



# Python利用itchat库向好友或者公众号发消息的实例
#
# 首先获得好友或者公众号的UserName
# 1. 获取好友UserName (给个人发送信息成功)
# import itchat
# itchat.auto_login(hotReload=True)
# #想给谁发信息，先查找到这个朋友,name后填微信备注即可,deepin测试成功
# users = itchat.search_friends(name='安西リ')
# #获取好友全部信息,返回一个列表,列表内是一个字典
# print(users)
# #获取`UserName`,用于发送消息
# userName = users[0]['UserName']
# itchat.send("hello 安西リ",toUserName = userName)

#获取所有好友信息
# account=itchat.get_friends()
# #获取自己的Username
# userName=account[0]['Username']

# 2. 获取公众号UserName (给公众号也测试发送成功)

import itchat
itchat.auto_login(hotReload=True)
# 返回完整的公众号列表
# mps = itchat.get_mps()
## 获取名字中含有特定字符的公众号，也就是按公众号名称查找,返回值为一个字典的列表
mps = itchat.search_mps(name="美食天下")
print(mps)
#发送方法和上面一样
userName = mps[0]['UserName']
itchat.send("品川、、",toUserName=userName)


# 3. 发送内容代码如下
# coding=utf8
import itchat

itchat.auto_login(hotReload=True)
# 获取通讯录信息
account = itchat.get_friends()
# #获取自己的UserName
userName = account[0]['UserName']
# 获取公众号信息
# mps = itchat.get_mps()
# print(mps)
lines = []
# 读取txt文件
f = open("/home/numb/Desktop/aaa.txt")
lines = f.readlines()  # 读取全部内容
# 循环发送文本内容
for i in range(90):
    # UserName需要用上面获取的自己修改
    itchat.send(lines[i], toUserName='UserName')
print("Success")