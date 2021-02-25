# 微信机器人Demo
# 导入相关模块
# from wxpy import *
#
# bot = Bot()  # 初始化
#
# bot.file_helper.send('testing~~~~~~')  # 发送信息给文件传输助手
# bot.file_helper.send_file('test.txt')  # 发送文件
# bot.file_helper.send_image('beauty.jpg')  # 发送图片

# bot.friends(update=True)  # 更新好友列表

# '''好友基本信息统计'''
# friends_list = bot.friends(True).search()  # 得到好友列表
# print(len(friends_list))  # 查看人数
# statics_result = bot.friends().stats_text()
# print(statics_result)
# '''获取指定好友头像并保存'''
# demo_friend = bot.friends().search("demo")[0]
# demo_friend.get_avatar('demon.jpg')
# favorite_girl = bot.friends().search("小娇贵")[0]
# favorite_girl.get_avatar('xiaohui.jpg')

# '''微信群基本信息统计'''
# groups_list = bot.groups().search()  # groups_list为一个
# print(len(groups_list))
# strugglegroup = bot.groups().search('好阁来煲仔饭')[0]
#
# '''打印出群成员'''
# print('打印群成员：')
# for member in strugglegroup:
#     print(member)

# '''自动处理消息'''
# '''type = TEXT/MAP/CARD/NOTE/SHARING/PICTURE/RECORDING/ATTACHMENT/VIDEO/FRIENDS/SYSTEM'''
# '''对于群消息，打印出来内容'''
#
#
# @bot.register(Group, TEXT)
# def print_group_msg(msg):
#     print(msg)



# '''好友文本消息'''
#
#
# @bot.register(Friend, TEXT)
# def reply_working_on(msg):
#     if msg.member == favorite_girl:
#         return
#     else:
#         return 'I am working now,Please wait a moment'


# '''图片消息'''
#
#
# @bot.register(Friend, PICTURE)
# def reply_good_news(msg):
#     return 'What a good photo!'
#
#
# '''视频消息'''
#
#
# @bot.register(Friend, VIDEO)
# def reply_nospare_time(msg):
#     return 'I am no time!'
#

# '''自动接受好友邀请'''
#
#
# @bot.register(msg_types=FRIENDS)
# def auto_accept_friends(msg):
#     if '你好' in msg.text.lower():
#         # 接受好友 (msg.card 为该请求的用户对象)
#         new_friend = bot.accept_friend(msg.card)
#         # 或 new_friend = msg.card.accept()
#         new_friend.send('你好，我自动接受了你的好友请求')


# @bot.register(favorite_girl, TEXT)
# def reply_to_beauty(msg):
#     return "You are so beautiful!"


# # 保持后台登录状态
# embed()
# bot.join()




from wxpy import *
bot = Bot()
strugglegroup = bot.groups().search('CUE日本留学生活')[0]



'''自动处理消息'''
'''type = TEXT/MAP/CARD/NOTE/SHARING/PICTURE/RECORDING/ATTACHMENT/VIDEO/FRIENDS/SYSTEM'''
'''对于群消息，打印出来内容'''
bot = Bot()

@bot.register(Group, TEXT)
def print_group_msg(msg):# 基本可以跟踪群消息，调整之后 捕获字段成功
    print(msg)
    str_msg = str(msg)
    if "日" in str_msg:
        bot.file_helper.send(msg)
        bot.file_helper.send("捕获字段成功")
    else:
        pass




if __name__=="__main__":
      # 初始化

    bot.file_helper.send('testing~~~~~~')  # 发送信息给文件传输助手
    print_group_msg(strugglegroup)

    embed()
    bot.join()