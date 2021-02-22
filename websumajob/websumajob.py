#! -*- coding:utf-8 -*-


import datetime
import re
import os
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import xlrd
from xlrd import xldate_as_tuple
import datetime
import pymysql
import requests
from lxml import etree
from requests.exceptions import RequestException

def call_page(url):

    driver.get(url)

    time.sleep(20)
    driver.find_element_by_xpath('//*[@id="username"]').clear()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys("")#用户名

    time.sleep(20)

    driver.find_element_by_xpath('//*[@id="password"]').clear()
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("")# 密码
    driver.find_element_by_xpath('//*[@id="app"]/div/header[2]/div/p[2]/button/span[1]').click()

    time.sleep(10)
    # 上面登陆没有问题



    # 选择年龄 解决下拉列表的问题

    # opt = driver.find_element_by_name('age_min')
    # Select(opt).select_by_visible_text('18')
    #
    #
    # opt = driver.find_element_by_name('age_max')
    # Select(opt).select_by_visible_text('20')
    #
    #
    #
    #
    # time.sleep(3)
    # driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul[1]/li[3]/button/span[1]').click()



    html = driver.page_source


    return html


def parse_pages(html):
    patt_t = re.compile('<div class="MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiInputBase-input MuiInput-input" tabindex="0" role="button" aria-haspopup="listbox" aria-labelledby="mui-component-select-date" id="mui-component-select-date">(.*?)</div>',re.S)
    item_t = re.findall(patt_t,html)
    patt = re.compile("</path></svg></i>(.*?)</p>",re.S)
    items = re.findall(patt,html)
    for item in item_t:
        big_list.append(item)
    for i in items:
        patt2 = re.compile("(.*?):(.*?)~(.*?):(.*?)",re.S)
        item =re.findall(patt2,i)
        if  len(item) !=0 :
            big_list.append(item)














def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))

       # # if 去掉表头
       # if rowNum > 0:


    return dataFile


def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")



if __name__ == '__main__':

    driver = webdriver.Chrome()
    url = 'https://web.sumajob.com/login'

    big_list = []
    html = call_page(url)
    parse_pages(html)
    print(big_list)