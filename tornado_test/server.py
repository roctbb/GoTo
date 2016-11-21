import tornado.ioloop
import tornado.web
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        f = open('reviews.json', 'r')
        text = f.read()
        f.close()

        cat_list = json.loads(text)
        self.render('review_list.html', cats=cat_list)

class ReviewHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
    def post(self):
        email = self.get_argument("email", "")
        name = self.get_argument("cat_name", "")
        review = self.get_argument("cat_review", "")
        galochka = self.get_argument("galochka", "no")

        if email!="" and name!="" and review!="":
            if galochka == "yes":
                galochka="да"
            else:
                galochka="нет"

            self.render('review.html', email=email, name=name, review=review, galochka=galochka)

            f = open('reviews.json', 'r')
            text = f.read()
            f.close()

            cat_list = json.loads(text)
            cat_list.append({"email": email, "name": name, "review": review, "ssit": galochka})
            text = json.dumps(cat_list)

            f=open("reviews.json", 'w')
            f.write(text)
            f.close()
        else:
            self.write("заполните все поля")


settings = [
    (r"/", MainHandler),
    (r"/save", ReviewHandler),
]

app = tornado.web.Application(settings)
app.listen(8000)
tornado.ioloop.IOLoop.current().start()