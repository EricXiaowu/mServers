from unittest import TestCase

import requests


class TestTornadoRequest(TestCase):
    base_url = 'http://10.36.174.5:8000'

    def test_index_get(self):
        url = self.base_url + '/'
        # 发起post请求，表单参数使用data来指定
        resp = requests.get(url, params={
            'wd': 'Eric',
            'title': ('西安', '湖北')
        })
        print(resp.text)

    def test_index_post(self):
        url = self.base_url + '/'
        # 发起post请求，表单参数使用data来指定
        resp = requests.post(url, data={
            'name': 'Eric',
            'city': '西安',
        })
        print(resp.text)



    def test_index_put(self):
        url = self.base_url + '/'
        # 发起post请求，表单参数使用data来指定
        resp = requests.put(url, data={
            'wd': 'Eric',
            'title': ('西安', '湖北')
        })
        print(resp.text)

    def test_index_delete(self):
        url = self.base_url + '/'
        # 发起post请求，表单参数使用data来指定
        resp = requests.delete(url, data={
            'wd': 'Eric',
            'title': ('西安', '湖北')
        })
        print(resp.text)


class TestOrderRequest(TestCase):
    url = 'http://10.36.174.5:8000/order/3/1'

    def test_get(self):
        resp = requests.get(self.url)
        print(resp.text)

    def test_post(self):
        resp = requests.post(self.url)
        print(resp.text)


class TestUserRequest(TestCase):
    url = 'http://10.36.174.2:8000/user'

    def test_login(self):
        # 上传json数据
        resp = requests.get(self.url,
                            json={
                                'name': 'jack',
                                'pwd': '123'
                            })

        # 读取响应的json数据
        print(resp.json())