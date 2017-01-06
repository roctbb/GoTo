import os
import random
import uuid

import tornado.ioloop
import tornado.web

from filter import process

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

        process('images/' + cname, 'results/' + cname)

        self.render('result.html', name=cname)




settings = [
    ('/', MainHandler),
    ('/results/(.*)', tornado.web.StaticFileHandler, {'path': 'results'}),
]
app = tornado.web.Application(settings)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()