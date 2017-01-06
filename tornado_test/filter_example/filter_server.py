import os
import random
import uuid

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('upload.html')
    def post(self):
        fileinfo = self.request.files['image'][0]
        fname = fileinfo['filename']
        extn = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + extn
        fh = open('images/' + cname, 'wb')
        fh.write(fileinfo['body'])
        #тут ваш фильтр на images/ cname . extn

        fh = open('results/' + cname, 'wb') #это временно, сохранить в result
        fh.write(fileinfo['body'])#должен ваш фильтр
        
        self.render('result.html', name=cname)




settings = [
    ('/', MainHandler),
    ('/results/(.*)', tornado.web.StaticFileHandler, {'path': 'results'}),
]
app = tornado.web.Application(settings)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()