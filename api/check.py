import os

import tornado.web


class CheckHandler(tornado.web.RequestHandler):

    def initialize(self, upload_dir):

        self.upload_dir = upload_dir

    async def get(self, file_uuid):

        if file_uuid is None:
            self.send_error(400, message="file_uuid ")

        file_path = os.path.join(self.upload_dir, file_uuid)
        file_exists = os.path.isfile(file_path)

        if file_exists:
            self.set_status(status_code=200)
        else:
            self.set_status(status_code=204)
