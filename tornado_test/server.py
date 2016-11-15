import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cute_cats = ['Дэдди', 'Ростик', 'Козиночка', 'Питер', 'Барсик']
        self.render('index.html', cats = cute_cats)

class GoodbyeHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name", "")
        self.write("Goodbye "+name+"!")

settings = [
    (r"/", MainHandler),
    (r"/goodbye", GoodbyeHandler),
]

app = tornado.web.Application(settings)
app.listen(8000)
tornado.ioloop.IOLoop.current().start()