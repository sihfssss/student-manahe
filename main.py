import manage

if __name__ == '__main__':
    while True:
        print("""
        1，录入成绩
        2. 查询成绩
        3，删除成绩
        4，修改信息
        5，查看成绩
        """)
        try:
            num = int(input())
        except ValueError:
            num = 0
            print("输入错误")

        if num == 1:
            manage.insert()

        elif num == 2:
            manage.search()

        elif num == 5:
            manage.look()

        elif num == 4:
            manage.modify()

        elif num == 3:
            manage.delete()
        else:
            break
