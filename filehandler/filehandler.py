import tornado.web
import logging
import os
import uuid
import json


class FileHandler(tornado.web.RequestHandler):

    def initialize(self, upload_dir):

        self.upload_dir = upload_dir

    @tornado.gen.coroutine
    def put(self):
        binary_data = self.request.body
        self.set_header('Content-Type', 'application/json')
        filename = str(uuid.uuid4())
        try:
            with open(os.path.join(self.upload_dir, filename), 'wb') as file:
                file.write(binary_data)
            logging.info("file uploaded , saved as %s",
                         filename)
            self.set_status(status_code=200)
            self.write(json.dumps({"file_uuid": filename}))

        except Exception as e:
            logging.error("Failed because %s", str(e))

    @tornado.gen.coroutine
    def get(self):

        file_uuid = self.request.headers.get('file_uuid')

        if file_uuid is None:
            self.send_error(400, message="file_uuid ")

        file_path = os.path.join(self.upload_dir, file_uuid)
        file_exists = os.path.isfile(file_path)

        if file_exists:

            buf_size = 4096
            self.set_header('Content-Type', 'application/octet-stream')
            self.set_header('Content-Disposition', 'attachment; filename=' + file_uuid)
            with open(file_path, 'r') as f:
                while True:
                    data = f.read(buf_size)
                    if not data:
                        break
                    self.write(data)
            self.finish()
            self.set_status(status_code=200)
        else:
            self.set_status(status_code=204)

    @tornado.gen.coroutine
    def head(self):
        file_uuid = self.request.headers.get('file_uuid')

        if file_uuid is None:
            self.send_error(400, message="file_uuid ")

        file_path = os.path.join(self.upload_dir, file_uuid)
        file_exists = os.path.isfile(file_path)

        if file_exists:
            self.set_status(status_code=200)
        else:
            self.set_status(status_code=204)
