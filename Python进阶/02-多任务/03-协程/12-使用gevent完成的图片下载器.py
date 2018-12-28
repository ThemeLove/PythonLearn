import gevent
from gevent import monkey
import urllib.request


monkey.patch_all()  # 将程序中用到的耗时操作的代码，切换为gevent中自己实现的模块


def download_image(url):
    req = urllib.request.urlopen(url)
    image_content = req.read()
    with open("meinv.jepg", "wb") as f:
        f.write(image_content)


gevent.joinall([  # 管理所有gevent任务
    # 创建一个gevent任务
    gevent.spawn(download_image, "https://i0.cdn.xiongmaoxingyan.com/ca717a55695f86b885ef35c4a348dc88_w338_h190.jpeg")
])