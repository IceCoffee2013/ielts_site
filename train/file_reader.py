#coding=utf8
from train import database

__author__ = 'Langley'

def read():
    file = open("../data/12306.txt")
    list = []
    for line in file:
        str = line.decode('gbk').split('----')
        mail = str[0]
        name = str[2]
        phone = str[5]
        cardId = str[3]
        userName = str[4]
        key = str[1]

        item = (mail,name,phone,cardId,userName,key)
        list.append(item)

        if len(list) > 1000:
            database.update(list)
            list = []

        # temp = []
        # temp.append(item)
        # database.update(temp)
        # print mail +';'+ name+';'+phone+';'+cardId+';'+userName+';'+key
        # print item[1]

    database.update(list)

    return list

def run():
    list = read()


run()