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
            if URL_FUNC_DICT[path]:
                response_body = URL_FUNC_DICT[path]()
            else:
                response_status_line_and_header = get_response_status_line_and_header("404", [("Server", "webserver"), ("Content-Type", "text/html;charset=utf8")])
                response_body = "404 没有找到相关资源"
        except Exception as e:
            response_status_line_and_header = get_response_status_line_and_header("500", [("Server", "webserver"), (
            "Content-Type", "text/html;charset=utf8")])
            response_body = "产生了异常"
    else:
        response_status_line_and_header = get_response_status_line_and_header("404", [("Server", "webserver"), ("Content-Type", "text/html;charset=utf8")])
        response_body = "404 没有找到相关资源"

    return response_status_line_and_header + response_body


@route("/index.py")
def index():
    with open("./static/index.html") as f:
        return f.read()


@route("/center.py")
def center():
    with open("./static/center.html") as f:
        return f.read()


