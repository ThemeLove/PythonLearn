from pymysql import connect


class JD:
    def __init__(self):
        """1.创建数据库连接
           2.获取数据库cursor
        """
        # 创建数据库连接
        self.conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='themelove', charset='utf8')
        # 获取cursor对象
        self.cursor = self.conn.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_goods(self):
        sql = """select * from goods;"""
        self.execute_sql(sql)

    def show_goods_cates(self):
        sql = """select * from goods_cates;"""
        self.execute_sql(sql)

    def show_goods_brands(self):
        sql = """select * from goods_brands;"""
        self.execute_sql(sql)

    def add_good_brand(self):
        brand_name = input("请输入您要添加的品牌名称：")
        # 通过给传参数的方式，让mysql自己拼接参数，可以防止sql语句注入
        sql = """insert into goods_brands(name) values(%s);"""
        self.cursor.execute(sql, (brand_name,))
        # 如果时增删改，需要用connect进行commit
        self.conn.commit()

    def search_good_brand_by_name(self):
        brand_name = input("请输入您要查询的品牌名称：")
        sql = """select name from goods_brands %s;"""
        # 不自己拼接参数，传参数给mysql让其自己拼接可以防止sql注入
        self.cursor.execute(sql, brand_name)
        for temp in self.cursor:
            print(temp)

        # 自己拼接参数可能发生sql语句注入：比如用户输入 '' or 1=1 ,会查询出所有品牌信息
        # sql = """select name from goods_brands %s;""" % brand_name
        # self.execute_sql(sql)

    @staticmethod
    def show_hint():
        print("-----京东商城-----")
        print("1:查看所有商品")
        print("2.产看所有商品分类")
        print("3.查看所有商品品牌")
        print("4.添加一个品牌")
        print("5.退出")
        return input("请输入您要操作的序号：")

    def run(self):
        while True:
            opt = self.show_hint()
            if opt == "1":
                self.show_all_goods()
            elif opt == "2":
                self.show_goods_cates()
            elif opt == "3":
                self.show_goods_brands()
            elif opt == "4":
                self.add_good_brand()
            elif opt == "5":  # 退出循环
                self.close()
                break
            else:
                print("请重新输入")


def main():
    # 创建JD对象
    jd = JD()
    # 调用jd的run方法
    jd.run()


if __name__ == "__main__":
    main()
