import re
import requests


def main():

    # 豆瓣具体帖子
    url = "https://www.douban.com/people/54274369/status/2423362195/comment"
    # url = "https://www.douban.com/group/topic/133914362/"
    # 豆瓣具体帖子回复的接口，格式是帖子链接+/add_comment
    # comment_url = url + "/add_comment"
    cookie ="bid=zUoAh8eCFA0; ap_v=0,6.0; __yadk_uid=v8ngXlKX6zD2FZCDdt3mR7KyYzl7Cq8g; __utmc=30149280; ll=\"108296\"; ck=2huL; douban-fav-remind=1; gr_user_id=8b0fccd0-37a9-49bc-9daf-13eee9ebc5c6; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=81ea600c-3776-4207-839e-3f8aae570887; gr_cs1_81ea600c-3776-4207-839e-3f8aae570887=user_id%3A1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_81ea600c-3776-4207-839e-3f8aae570887=true; _vwo_uuid_v2=D74B56794702EAE778598815B56C9982A|4e79f495207ddc9618b38b0a827f615e; douban-profile-remind=1; _pk_id.100001.8cb4=3f9e841f0d023e01.1551757593.1.1551759709.1551757593.; _pk_ses.100001.8cb4=*; push_doumail_num=0; __utma=30149280.250398097.1551757594.1551757594.1551757594.1; __utmz=30149280.1551757594.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=30149280.18958; __utmb=30149280.49.7.1551759397082; push_noty_num=1"
    referer = "https://www.douban.com/people/54274369/status/2423362195/?start=0"

    agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'
    headers = {
        "Host": "www.douban.com",
        "Referer": referer,
        'User-Agent': agent,
        "Cookie": cookie,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
    ck =re.findall("ck=(.*?);", headers["Cookie"])[-1]
    print("ck="+ck)
    params = {
        "text": '楼主大才，请收下我的膝盖',
        # "ck":"2huL",
        "ck": re.findall("ck=(.*?);", headers["Cookie"])[-1],
    }
    requests.packages.urllib3.disable_warnings()
    response = requests.post(url, headers=headers, allow_redirects=False,
                             data=params, verify=False)
    print("response="+str(response.content))


if __name__ == "__main__":
    main()
