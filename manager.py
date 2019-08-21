import json

import tornado.web
import tornado.ioloop
import tornado.options
from tornado.httputil import HTTPServerRequest


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # 请求参数读取
        # 读取单个参数
        wd = self.get_argument('wd')
        print(wd)

        # 读取多个参数名相同的参数
        titles = self.get_arguments('title')

        # 从查询参数中读取url路径参数
        wd2 = self.get_query_argument('wd')
        print(wd2)
        titles2 = self.get_query_arguments('title')
        print(titles2)

        print(titles)

        # 从请求对象中读取参数
        req: HTTPServerRequest = self.request
        # request请求中的数据都是dict字典类型
        wd3 = req.arguments.get('wd')
        print(wd3)  # 字典key对应的value都是bytes字节类型

        wd4 = req.query_arguments.get('wd')
        print(wd4)

        self.write('<h3>我的主页 %s, %s</h3>' % (wd, titles))

    def post(self):

        # 新增数据
        # 读取表单参数
        # wd6 = self.get_arguments('name')
        # wd7 = self.get_arguments('city')

        name = self.get_body_argument('name')
        city = self.get_body_argument('city')

        self.write('<h3>POST请求方法</h3>%s,%s' % (name, city))

    def put(self):

        self.write('<h3>PUT请求方法</h3>')

    def delete(self):

        self.write('<h3>DELETE请求方法</h3>')


class SearchHandler(tornado.web.RequestHandler):
    mapper = {
        'python': 'Python是目前世界最流行的AI语言',
        'java': 'Java已经是20多年企业级应用开发语言',
        'H5': 'H5全称是HTML5，于2014流程的前端WEB开发标签语言'
    }

    def get(self):
        html = """
            <h3>搜索%s的结果</h3>
            <p>
                %s
            </p>
        """
        wd = self.get_query_argument('wd')
        result = self.mapper.get(wd)

        # self. write(htmI % (wd, result) )
        resp_data = {
            'wd': wd,
            'result': result
        }

        self.write(json.dumps(resp_data))
        self.set_status(200)   # 设置响应状态码
        # 设置响应头的数据类型
        self.set_header('Content-Type', 'application/json;charset=utf-8')

        # cookie操作
        self.set_cookie('wd', wd)


class CookieHandler(tornado.web.RequestHandler):
    def get(self):
        # 验证参数中是否存在 name
        if self.request.arguments.get('name'):
            # 从查询参数中读取Cookie的名称
            name = self.get_query_argument('name')

            # 从cookies中获取name的对象或值
            value = self.get_cookie(name)
            print(type(value))
            self.write(value)
        else:
            # 查看所有的cookie
            cookies: dict = self.request.cookies
            html = '<ul>%s</ul>'
            lis = []
            for key in cookies:

                lis.append('<li>%s: %s</li>' % (key, self.get_cookie(key)))

            html = '显示所有cookie' + html % ''.join(lis)
            html += """
                <form method="post">
                    <input name="name" placeholder="请输入cookie的名称">
                    <button>提交</button>
                </form>
            """
            self.write(html)

    def delete(self):
        name = self.get_argument('name')
        if self.request.cookies.get(name, None):
            # 存在的
            self.clear_cookie(name)
            self.write('<h3 style>删除%s成功' % name)
        else:
            self.write('删除^%s失败，不存在!' % name)


class OrderHandler(tornado.web.RequestHandler):

    goods = [
        {
            'id': 1,
            'name': 'python开发',
            'author': 'Eric',
            'price': 3000,
        },
        {
            'id': 2,
            'name': 'python开发',
            'author': 'Eric',
            'price': 3000,
        }
    ]
    action_map = {
        1: '取消订单',
        2: '再次购买',
        3: '评价',
    }

    def query(self, order_id):
        for item in self.goods:
            if item. get('id') == order_id:
                return item

    def initialize(self):
        # 所有的请求方法在调用之前，都会进行初始化操作
        print('---------initialize----------')

    def prepare(self):

        print('--------prepare----------')

    def get(self, order_id, action_code):
        self. write('订单查询')
        html = ("""
            <p>
                商品编号:%s
            </p>
            <p>
                商品名称:%s
            </p>.
            <p>
                商品价何:%s
            </p>
        """)

        goods = self.query(int(order_id))
        self.write(html % (goods.get('id'), goods.get('name'), goods.get('price')))
        self.write(self.action_map.get(action_code))

        self.write('订单查询')

    def post(self, action_code, order_id):
        self.write('------post------')

    def on_finish(self):
        print('----------on_finish-----------')


def make_app():
    return tornado.web.Application([
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(?P<action_code>\d+)/(?P<order_id>\d+)', OrderHandler)
    ], default_host=tornado.options.options.host)


if __name__ == '__main__':
    tornado.options.define('port',
                           default=8000,
                           type=int,
                           help='绑定socket端口')
    tornado.options.define('host',
                           default='localhost',
                           type=str,
                           help='设置host参数')

    # 解析命令行参数
    tornado.options.parse_command_line()
    app = make_app()
    app.listen(tornado.options.options.port)
    print('starting Web Server Http://%s:%s' % (
        tornado.options.options.port,
        tornado.options.options.host
    ))
    # 启动服务
    tornado.ioloop.IOLoop.current().start()
