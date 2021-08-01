#database statements(build db/table):
#create database crawler character set UTF8 collate utf8_bin;
#create table hotnews(ID int not null AUTO_INCREMENT PRIMARY KEY, title varchar(255),link varchar(255),  
#source varchar(16), creation_time  DATETIME DEFAULT   CURRENT_TIMESTAMP);

import pymysql
import time
import datetime

#database statements(build db/table):
#create database crawler character set UTF8 collate utf8_bin;
#create table hotnews(ID int not null AUTO_INCREMENT PRIMARY KEY, title varchar(255),link varchar(255),  
#source varchar(16), creation_time  DATETIME DEFAULT   CURRENT_TIMESTAMP);


def timer(func):
    def proxy(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        d_time = end_time - start_time
        print("the running time is : ", d_time)
    return proxy

@timer
def insert_multiple_news(news):
    conn = pymysql.connect(
        host="localhost",
        user="test",
        password="123456",
        database="crawler",
        charset='utf8'
    )
    cs = conn.cursor()
    # news = [(item.title, item.comment.link, item.source.name) for item in items]
    try:
        print(news)
        sql = "INSERT INTO hotnews (title, link, source, s_title, s_link, ner, kw, hot) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
        cs.executemany(sql, news)
        conn.commit()
    except:
        conn.rollback()
        raise

    cs.close()
    conn.close()

def insert_single_news(news):
    conn = pymysql.connect(
        host="localhost",
        user="test",
        password="123456",
        database="crawler",
        charset='utf8'
    )
    cs = conn.cursor();

    try:
        # paras = ("kw", "ner", news)
        if len(eval(news[-3])) <= 0:
            sql = "INSERT INTO hotnews (title, link, source, s_title, s_link, ner, kw, hot) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
            cs.execute(sql, news)
        else:
            sql = "SELECT count(*) FROM hotnews WHERE title = %s"
            cs.execute(sql, news[0])
            rst = cs.fetchone()
            count = rst[0]
            if count > 0:
                print("Duplicate!" + str(news))
                return
            sql = "SELECT * FROM hotnews WHERE ner = %s"
            cs.execute(sql, news[-3])
            rst = cs.fetchall()
        
            if len(rst) > 0:
                for r in rst:
                    shared = list(set(eval(r[-3])).intersection(set(eval(news[-2]))))
                    print(shared)
                    if len(shared) > 0:
                        # print(time.strftime("%Y-%m-%d %H:%M:%S"))
                        diff = days(time.strftime("%Y-%m-%d %H:%M:%S"), str(r[3]))
                        print(diff, r[-2])
                        hot = pow(8/10, diff) * int(r[-2]) + news[-1]
                        print(hot)
                        hot = min(5, hot)
                        sql = "UPDATE hotnews SET hot = %s, update_time = now() WHERE ner = %s"
                        cs.execute(sql, (hot, news[-3]))
                        break
                    else:
                        sql = "INSERT INTO hotnews (title, link, source, s_title, s_link, ner, kw, hot) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                        cs.execute(sql, news)
            else:
                sql = "INSERT INTO hotnews (title, link, source, s_title, s_link, ner, kw, hot) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                cs.execute(sql, news)
            conn.commit()
    except:
        print("Exception" + str(news))
        conn.rollback()

    cs.close()
    conn.close()


def days(str1,str2):
    date1=datetime.datetime.strptime(str1[0:10],"%Y-%m-%d")
    date2=datetime.datetime.strptime(str2[0:10],"%Y-%m-%d")
    num=(date1-date2).days
    return num

# print(days("2021-07-31 20:01:57", "2021-07-30 20:01:57"))
# print(str(get_select_statement).format("kw, hot", "ner", a))