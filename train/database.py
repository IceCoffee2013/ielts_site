#coding=utf8

# database operation
# query seat before, if different or empty, set or add.
import MySQLdb
import sys
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

def update(list):
    try:
        # conn = MySQLdb.connect(host='localhost',user='root',passwd='12345',port=3306,charset="utf8") # mysql default latin-1
        conn = MySQLdb.connect(host='joinzhou.mysql.rds.aliyuncs.com',user='huoche',passwd='huoche',port=3306,charset="utf8") # mysql default latin-1
        cur = conn.cursor(MySQLdb.cursors.DictCursor)

        conn.select_db('huoche')

        # values = []
        # for i in list:
        #     item = tuple((i[0], i[1], i[2], i[3], i[4], i[5]))   # name, date, province, city, seat_id, status):
        #     values.append(item)

        # cur.executemany('replace into train_account values(%s, %s, %s, %s, %s, %s)', list)
        cur.executemany('insert into huoche_user values(%s, %s, %s, %s, %s, %s, %s)', list)

        count = cur.execute('select * from huoche_user')
        print 'Count: '+str(count)

        cur.close()
        conn.commit()
        conn.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])