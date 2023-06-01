import random
import sqlite3


def start(name, age, class_, math, chinese, english):
    cnn = sqlite3.Connection("student" + ".db")
    db = cnn.cursor()
    db.execute(
        f"insert into student(name, age, class, math, chinese, english) values(?, ?, ?, ?, ?, ?)",
        (name, age, class_, math, chinese, english))
    cnn.commit()
    cnn.close()


if __name__ == '__main__':
    f_name = ['张', '王', '李', '刘', '陈', '杨', '赵', '黄', '周', '吴', '郑', '朱', '许', '沈', '潘', '胡', '刘',
              '田', '言', '唐', '罗', '贺', '毛', '姚', '崔', '薛', '钟', '刘', '廖', '邓', '马', '戴', '于', '赵',
              '乔', '叶', '任', '鲁', '易', '苏', '潘', '范', '石', '石', '刘', '崔', '唐', '魏', '冯', '牛']
    n = 0
    while n < 51:
        name = f"{random.choice(f_name)}{random.choice(f_name)}"
        start(name, random.randint(1, 50), f"{random.randint(1, 9)}年{random.randint(1, 5)}班", random.randint(50, 120),
              random.randint(50, 120), random.randint(50, 120))
        n += 1
        print(f"添加了{n}个")
