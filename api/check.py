import os

import tornado.web


class CheckHandler(tornado.web.RequestHandler):

    def initialize(self, upload_dir):

        self.upload_dir = upload_dir

    def get(self, file_uuid):

        file_path = os.path.join(self.upload_dir, file_uuid)
        file_exists = os.path.isfile(file_path)

        if file_exists:
            self.set_status(status_code=200)
        else:
            self.set_status(status_code=204)
