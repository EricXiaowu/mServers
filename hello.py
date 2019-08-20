from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler


class IndexHanderler(RequestHandler):
    def get(self):
        # 向客户端响应数据
        self.write('<h3>Hello,Tornado</h3>')


if __name__ == '__main__':
    # 创建WEB应用
    app = Application([
        ('/', IndexHanderler)
    ])
    # 绑定端口
    app.listen(7000)    # 端口 < 65535

    # 启动WEB端口
    print('starting http://localhost:%s' % 7000)
    IOLoop.current().start()
