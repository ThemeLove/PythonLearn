import gevent
from gevent import monkey
import urllib.request


monkey.patch_all()


def download_image(url):
    req = urllib.request.urlopen(url)
    image_content = req.read()
    with open("meinv.jepg", "wb") as f:
        f.write(image_content)


gevent.joinall([
    gevent.spawn(download_image, "https://i0.cdn.xiongmaoxingyan.com/ca717a55695f86b885ef35c4a348dc88_w338_h190.jpeg")

])