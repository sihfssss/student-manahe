import sqlite3
from sqlite3 import OperationalError

import logger

logges = logger.Logger()


def delete():
    name = input("你要删除学生的姓名: ")
    Manage().delete(name)


def search():
    name = input("请输入您要查询的学生名称")
    Manage().search(name)


def modify():
    old_name = input("请输入要修改的姓名: ")
    new_name = input("您要修改成的名字:")
    age = input("请输入要修改的年龄: ")
    class_ = input("请输入班级: ")
    chinese = input("请输入语文成绩: ")
    math = input("请输入数学: ")
    english = input("请输入英语成绩")
    Manage().modify(new_name, age, class_, chinese, math, english, old_name)


def insert():
    name = input("请输入姓名: ")
    age = input("请输入年龄: ")
    class_ = input("请输入班级: ")
    chinese = input("请输入语文成绩: ")
    math = input("请输入数学: ")
    english = input("请输入英语成绩")
    Manage().connect(name, age, class_, chinese, math, english)


def look():
    lists = Manage().look()
    print(lists)


class Manage:
    def __init__(self):
        self.dataName = "Student"

    def connect(self, name, age, class_, math, chinese, english):
        try:
            cnn = sqlite3.Connection(self.dataName + ".db")
            db = cnn.cursor()
            db.execute(
                f"insert into {self.dataName}(name, age, class, math, chinese, english) values(?, ?, ?, ?, ?, ?)",
                (name, age, class_, math, chinese, english))
            cnn.commit()
            cnn.close()
            logges.success("储存成功")
        except OperationalError:
            logges.success("正在创建数据库")
            self.create_database()
            logges.success("创建成功")
            logges.info("请重新输入")

    def look(self):
        cnn = sqlite3.Connection(self.dataName + ".db")
        db = cnn.cursor()
        db.execute(f"select * from {self.dataName}")
        lists = db.fetchall()
        cnn.commit()
        cnn.close()
        return lists

    def create_database(self):
        cnn = sqlite3.Connection(self.dataName + ".db")
        db = cnn.cursor()
        db.execute(f"""CREATE TABLE {self.dataName} (
                  id SERIAL PRIMARY KEY,
                  name varchar(225),
                  age int,
                  class varchar(225),
                  math int,
                  chinese int,
                  english int
                );""")
        cnn.commit()
        cnn.close()

    def modify(self, name, age, class_, math, chinese, english, old_name):
        cnn = sqlite3.Connection(self.dataName + ".db")
        db = cnn.cursor()
        db.execute(
            f"UPDATE {self.dataName} SET name = ?, age = ?, class = ?, math = ?, chinese = ?, english = ? WHERE name = ?;",
            (name, age, class_, math, chinese, english, old_name))
        cnn.commit()
        db.execute(f"select * from {self.dataName} where name = ?", (name,))
        modify_data = db.fetchall()
        cnn.commit()
        cnn.close()
        if not modify_data:
            randoms = input("没有改同学是否添加(yes/no): ")
            if randoms == "yes":
                self.connect(name, age, class_, math, chinese, english)
            else:
                print("正在返回主页")
        else:
            logges.success("修改成功")
            print("已修改为: " + str(modify_data))

    def search(self, name):
        cnn = sqlite3.Connection(self.dataName + ".db")
        db = cnn.cursor()
        db.execute(f"select * from {self.dataName} where name = ?", (name,))
        lists = db.fetchall()
        cnn.commit()
        cnn.close()
        if not lists:
            print("没有此学生")
        else:
            print(lists)

    def delete(self, name):
        cnn = sqlite3.Connection(self.dataName + ".db")
        db = cnn.cursor()
        db.execute(f"select * from {self.dataName} where name = ?", (name,))
        search_list = db.fetchall()
        cnn.commit()
        if not search_list:
            print("没有这个人")
        else:
            db.execute(f"delete from {self.dataName} where name = ?", (name,))
            cnn.commit()
            cnn.close()
            logges.info("删除成功")
            look()

