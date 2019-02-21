from urllib.parse import quote
from urllib.parse import unquote
from urllib.parse import urlencode


def main():

    # urlencode(dict) 参数为字典，会先将字典转化为key=value&key1=value1....的字符串，在对其进行url编码
    dict_a = {"name": "zhangsan", "age": 23, "gender": "男"}
    encode_str = urlencode(dict_a)
    print("type of encode_str =" + str(type(encode_str)))
    print("encode_str="+encode_str)

    # 注意没有urldecode模块，urlencode的字典解码要用quote解码，解码后为key=value&key1=value1....的字符串
    unquote_str = unquote(encode_str)
    print("unquote_str="+unquote_str)

    # quote可以单独对字符串进行编码
    str2 = "刻苦"
    quote_str2 = quote(str2)
    print("type of quote_str2"+str(type(quote_str2)))
    print("quote_str2="+quote_str2)

    # unquote对quote编码过的字符串解码
    unquote_str2 = unquote(quote_str2)
    print("unquote_str2="+unquote_str2)


if __name__ == "__main__":
    main()
