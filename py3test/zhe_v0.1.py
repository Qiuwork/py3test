#_*_ coding:utf-8 _*_
# Author: Qiu

"""
作业内容：
    实现一个图片下载器，读取url文件内容，顺序下载图片，支持通过len()、str()、iter()等函数。使用效果如下：
    e.g.
        imagedownloader = ImageDownloader('url.txt')
        imagedownloader.run()
        print(len(imagedownloader))     #=> 打印下载成功的图片数量
        print(imagedownloader)          #=> 打印类名 和 url文件的路径信息。 如：<ImageDownloader /path/to/url/text>
        for img in imagedownloader:
            print(img)      # 打印图片保存地址
要求：
    基于如下已有代码进行功能实现，其中图片内容下载相关代码已经实现。需要自己保存并维护图片文件路径。其它方法和属性需要自行添加。
"""

import re, sys, requests, os, time
from urllib.parse import quote
from collections import Iterable
from contextlib import closing


def crawl_url(keyword, pages):
    '''
    前期准备，获取资源url
    :param keyword: 关键字
    :param pages: 需要获取的总页数
    :return: url列表
    '''
    url_list = []
    for page in range(0,pages):
        word = quote(keyword, 'utf-8')
        pn = str(page * 20)
        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' \
               + word + '&ct=201326592&ic=0&lm=-1&width=&height=&v=flip&pn=' \
               + pn
        try:
            rep = r'"objURL":"(.*?)"'
            respone = requests.get(url, timeout=30)
            p_list = re.findall(rep, respone.text, re.S)
            url_list.extend(p_list)
        except Exception as e:
            print(e)
    return url_list

#
def write_url_in_file(url_list, file):
    '''
    前期准备，获取资源url
    :param url_list: crawl_url的返回值
    :param file: 存储的文件名
    :return: 无意义
    '''
    if not isinstance(url_list, Iterable):
        return
    try:
        with open(file, 'w') as f:
            for url in url_list:
                f.write(url.strip() + '\r\n')
        print('Done')
        return 'ok'
    except Exception as e:
        print(e)
        return


class ImageDownloader(object):
    def __init__(self, url_file_name, dirname):
        self.url_file_name = url_file_name
        self.i = 0
        self.j = 0
        self.url_list = []
        self.dirname = dirname


    def mkdir(self, dirname):
        a = os.path.join(os.path.abspath('..'), dirname)
        if not os.path.exists(a):
            return os.mkdir(a)
        if not os.path.isfile(a):
            os.remove(a)
            return os.mkdir(a)
        return

    @staticmethod
    def download_image_by_url(url):
        def img_Path(url):
            reg = r'(?<=/)[^/]+jpg'
            prog = re.compile(reg)
            result = prog.search(url)
            filename = result.group()
            if not filename:
                return
            imgpath = os.path.join(os.path.abspath('..'), 'img', filename)
            return imgpath
        try:
            rep = requests.head(url)
            if not rep.headers.get('content-type').startswith('image/'):
                return
            imgpath = img_Path(url)
            if not imgpath:
                return
            if os.path.exists(imgpath):
                return
            rep = requests.request('GET', url, stream=True)
            with closing(rep) as rep:
                with open(imgpath, 'wb') as img:
                    for data in rep.iter_content(128):
                        img.write(data)
            return imgpath
        except:
            print(f'Request Fail For URL {url}')
            return

    def urls_list(self):
        filepath = os.path.join(os.getcwd(), self.url_file_name)
        with open(filepath, 'r') as f:
            for url in f.readlines():
                url = url.strip()
                if url:
                    self.url_list.append(url)
        return self.url_list

    def __len__(self):
        return self.j

    def __str__(self):
        filepath = os.path.join(os.getcwd(), self.url_file_name)
        return '类名：{0}, 文件存储路径：{1}'.format(self.__class__.__name__, filepath)

    def __iter__(self):
        self.urls_list()
        # print(self.url_list)
        return self

    def __next__(self):
        if self.i < len(self.url_list):
            b = self.url_list[self.i]
            self.i += 1
            imgpath = self.download_image_by_url(b)
            if imgpath:
                self.j += 1
                return imgpath
        else:
            raise StopIteration()

    def run(self):
        if not os.path.exists(os.path.join(os.path.abspath('..'), self.dirname)):
            self.mkdir(self.dirname)
        for img in self:
            if img:
                print(img)



keyword = '美女'
page_num = 1
file = 'urls.txt'
dirname = 'img'
a = crawl_url(keyword, page_num)
write_url_in_file(a, file)
a = time.time()
imageDownloader = ImageDownloader(file,dirname)
imageDownloader.run()
print(len(imageDownloader))
print(imageDownloader)
b = time.time()
print(b-a)


