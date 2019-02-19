import pymysql
import re
import logging


URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


def application(client_params, get_response_status_line_and_header):
    print("mini_frame----->application")
    print("client_params", client_params)
    if client_params:
        response_status_line_and_header = get_response_status_line_and_header("200", [("Server", "webserver"), ("Content-Type", "text/html;charset=utf8")])
        path = client_params["path"]

        try:
            for url, func in URL_FUNC_DICT.items():
                ret = re.match(url, path)
                if ret:
                    return response_status_line_and_header+ func(ret)
        except Exception as e:
            logging.exception(e)
            response_status_line_and_header = get_response_status_line_and_header("500", [("Server", "webserver"), (
                "Content-Type", "text/html;charset=utf8")])
            response_body = "产生了异常,没有该视图函数"
    else:
        response_status_line_and_header = get_response_status_line_and_header("404", [("Server", "webserver"), ("Content-Type", "text/html;charset=utf8")])
        response_body = "404 没有找到相关资源"

    return response_status_line_and_header + response_body


@route(r"/index\.html")
def index(ret):
    content = ""
    with open("./templates/index.html") as f:
        content = f.read()

    conn = pymysql.connect(host="localhost", port=3306, user="root", password="themelove", database="stock_db", charset="utf8")
    cursor = conn.cursor()

    sql = """select * from info;"""
    cursor.execute(sql)
    all_stock_info = cursor.fetchall()


    tr_template = """
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <input type="button" class="%s" value="%s" id="toAdd" name="toAdd" systemidvalue="%s">
        </td>
    </tr>
    """

    html_str = ""
    for line_info in all_stock_info:
        # 判断该只股票是否被关注
        sql_stock_is_has_focus = """select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s"""
        cursor.execute(sql_stock_is_has_focus, (line_info[1],))

        if cursor.fetchone():
            focus_str = "取关"
            class_str = "focus_off"
        else:
            focus_str = "关注"
            class_str = "focus_on"

        html_str += tr_template % (line_info[0], line_info[1], line_info[2], line_info[3], line_info[4], line_info[5], line_info[6], line_info[7], class_str, focus_str, line_info[1])
    conn.close()
    cursor.close()

    content = re.sub("{%content%}", html_str, content)

    return content


@route(r"/center\.html")
def center(ret):
    content = ""
    with open("./templates/center.html") as f:
        content = f.read()

    conn = pymysql.connect(host="localhost", port=3306, user="root", password="themelove", database="stock_db",
                           charset="utf8")
    cursor = conn.cursor()

    sql = """select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i inner join focus as f on i.id=f.info_id;"""
    cursor.execute(sql)
    all_stock_info = cursor.fetchall()
    cursor.close()
    conn.close()

    tr_template = """
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"><span aria-hidden="true"></span> 修改 </a>
        </td>
        <td>
            <input type="button" class="focus_off" value="取关" id="toDel" name="toDel" systemidvalue="%s">
        </td>
    </tr>
    """

    html_str = ""
    for line_info in all_stock_info:
        html_str += tr_template % (
        line_info[0], line_info[1], line_info[2], line_info[3], line_info[4], line_info[5], line_info[6],
        line_info[0], line_info[0])

    content = re.sub("{%content%}", html_str, content)

    return content


@route(r"/add/(\d+)\.html")
def add_focus(ret):
    """添加指定股票到关注列表"""
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="themelove", database="stock_db", charset="utf8")
    cursor = conn.cursor()
    stock_code = ret.group(1)
    print("stock_code=", stock_code)
    # 1.判断是否存在该只股票
    sql_is_has_stock="""select * from info where code=%s"""
    cursor.execute(sql_is_has_stock, (stock_code,))
    if not cursor.fetchone():  # 没有该只股票
        conn.close()
        cursor.close()
        return "没有该只股票，创业公司，请大哥手下留情"

    # 2.判断是否已经关注了该只股票
    sql_is_focus_stock = """select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s"""
    cursor.execute(sql_is_focus_stock, (stock_code,))
    if cursor.fetchone(): # 说明已经关注过该只股票
        conn.close()
        cursor.close()
        return "已经关注过该只股票，请勿重复关注"

    # 3.关注该只股票
    try:
        sql_focus_stock = """insert into focus values(default, %s, (select id from info where code=%s))"""
        cursor.execute(sql_focus_stock, ("不错哦", stock_code))
        conn.commit() # 修改操作要提交，pymysql默认开启了事物
        conn.close()
        cursor.close()
        return "关注股票(%s)成功！" % (stock_code,)
    except Exception as e:
        logging.exception(e)
        return "关注失败，请稍后再试"
