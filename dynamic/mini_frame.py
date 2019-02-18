def application(client_params, get_response_status_line_and_header):
    print("mini_frame----->application")
    print("client_params", client_params)
    if client_params:
        response_status_line_and_header = get_response_status_line_and_header("200", [("Content-Type", "text/html;charset=utf8")])
        path = client_params["path"]
        if path == "/index.py":
            response_body = index()
        elif path == "/center.py":
            response_body = center()
        else:
            response_status_line_and_header = get_response_status_line_and_header("404", [("Content-Type", "text/html;charset=utf8")])
            response_body =  "404 没有找到相关资源"
    else:
        response_status_line_and_header = get_response_status_line_and_header("404", [("Content-Type", "text/html;charset=utf8")])
        response_body = "404 没有找到相关资源"

    return response_status_line_and_header + response_body


def index():
    with open("./templates/index.html") as f:
        return f.read()


def center():
    with open("./templates/center.html") as f:
        return f.read()


