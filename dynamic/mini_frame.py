def application(client_params, set_response_header):
    print("mini_frame----->application")
    print("client_params", client_params)
    if client_params:
        set_response_header("200", [("Content-Type", "text/html;charset=utf8")])
        path = client_params["path"]
        if path == "/index.py":
            return index()
        elif path == "/center.py":
            return center()
        else:
            set_response_header("404", [("Content-Type", "text/html;charset=utf8")])
            return "404 没有找到相关资源"
    else:
        set_response_header("404", [("Content-Type", "text/html;charset=utf8")])
        return "404 没有找到相关资源"


def index():
    with open("./templates/index.html") as f:
        return f.read()


def center():
    with open("./templates/center.html") as f:
        return f.read()


