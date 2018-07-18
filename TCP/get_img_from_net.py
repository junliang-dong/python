# _*_ coding: utf-8 _*_
import urllib
import re
import os
import urllib.request
import ssl


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('utf-8')


def mkdir(path):
    path = path.strip()
    isExists = os.path.exists(path)

    if not isExists:
        print('新建目录：', path)
        os.makedirs(path)
        return True
    else:
        print('目录', path, '已存在')
        return False


def saveImages(imglist, path):
    number = 1
    for imageURL in imglist:
        print('image url:', imageURL)
        urllib.request.urlretrieve(imageURL, '{}{}.jpg'.format(path, number))
        number = number + 1


def getAllImg(html):
    reg = r'src=".+?\.jpg" pic_ext'
    imgre = re.compile(reg)
    imgList = imgre.findall(html)
    return imgList


if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    html = getHtml('https://tieba.baidu.com/p/2460150866')
    path = 'D:\\WorkSpace\\pictures\\'
    mkdir(path)
    imgList = getAllImg(html)
    saveImages(imgList, path)
