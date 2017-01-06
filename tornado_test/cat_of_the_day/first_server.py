import random

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<form method='get' action='/hello'><input name='name' /></form>")

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name", "Анон")
        self.write("<h1>Привет, "+name+"!</h1>")

class CatsHandler(tornado.web.RequestHandler):
    def get(self):
        cats = [
            ('Васька', '/static/1.jpg'),
            ('Петька', '/static/2.jpg'),
            ('Пушок', '/static/2.jpg'),
        ]
        cat = random.choice(cats)
        self.render("cats.html", cat_name=cat[0], cat_address=cat[1])
settings = [
    ('/', MainHandler),
    ('/hello', HelloHandler),
    ('/cats', CatsHandler),
    ('/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
]
#http://host:port/module/page/?param1=value1&param2=value2

app = tornado.web.Application(settings)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()