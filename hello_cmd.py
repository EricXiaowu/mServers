from tornado import web, ioloop

from tornado.options import define, options, parse_command_line
define('port', default=8000, type=int, help='设置Web服务的端口！')


class IndexHandler(web.RequestHandler):
    def get(self):
        word = self.get_argument('wd')
        self.write('Hello, Tornado <p>查询参数wd: %s</p>' % word)

    def post(self):
        word = self.get_argument('wd')
        self.write('Hello POST <p>查询参数wd: %s/p>' % word)


class LoginHandler(web.RequestHandler):
    def get(self):
        self.write('login')


class LogoutHandler(web.RequestHandler):
    def get(self):
        self.write('logout')


if __name__ == '__main__':
    parse_command_line()
    app = web.Application([
        ('/', IndexHandler),
        ('/login', LoginHandler),
        ('logout', LogoutHandler),
    ])
    app.listen(options.port)
    ioloop.IOLoop.current().start()
