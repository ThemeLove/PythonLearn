def application(client_params, set_response_header):
    print("mini_frame----->application")
    print("client_params", client_params)
    if client_params:
        set_response_header("200", [("Content-Type", "text/html;charset=utf8")])
        path = client_params["path"]
        if path == "/index.py":
            return index()
        elif path == "/make.py":
            return make()
        elif path == "/login.py":
            return login()
        else:
            set_response_header("404", [("Content-Type", "text/html;charset=utf8")])
            return "404 没有找到相关资源"
    else:
        set_response_header("404", [("Content-Type", "text/html;charset=utf8")])
        return "404 没有找到相关资源"


def index():
    with open("./foods/pages/index.html") as f:
        return f.read()


def make():
    with open("./foods/pages/make.html") as f:
        return f.read()


def login():
    with open("./foods/pages/login.html") as f:
        return f.read()
