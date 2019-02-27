import json
import os

import tornado.ioloop
import tornado.web
from api import check, download, upload


class HelloWorld(tornado.web.RequestHandler):
    def get(self):
        json.dumps({"server": 'Tornado File Storage API v0.3'})
        self.write(json.dumps({"server": 'Tornado File Storage API v0.3'}))


def get_app():
    port = 9999
    file_storage_path = "storage"

    if not os.path.exists(file_storage_path):
        os.mkdir(file_storage_path)

    # TODO : Bad request handling via validation
    # TODO : add  re.IGNORECASE for uuid validation


    app = tornado.web.Application([
        (r"/check/([a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89aAbB][a-f0-9]{3}-[a-f0-9]{12})", check.CheckHandler,
         dict(upload_dir=file_storage_path)),
        (r"/download/([a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89aAbB][a-f0-9]{3}-[a-f0-9]{12})", download.DownloadHandler,
         dict(upload_dir=file_storage_path)),
        (r"/upload", upload.UploadHandler, dict(upload_dir=file_storage_path)),
        (r"/", HelloWorld)
    ])

    app.listen(port)
    return app


def start_server():
    get_app()
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    start_server()
