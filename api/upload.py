import io
import json
import os
import uuid

import tornado.web

MAX_STREAMED_SIZE = 1024 * 1024 * 1024
CHUNK_SIZE = 1024 * 1024 * 1  # 1 MiB


@tornado.web.stream_request_body
class UploadHandler(tornado.web.RequestHandler):
    def initialize(self, upload_dir):
        self.bytes_read = 0
        self.data = b''
        self.upload_dir = upload_dir

    def prepare(self):
        self.request.connection.set_max_body_size(MAX_STREAMED_SIZE)

    def data_received(self, chunck):
        self.bytes_read += len(chunck)
        self.data += chunck

    def post(self):

        filename = str(uuid.uuid4())

        file_path = os.path.join(self.upload_dir, filename)

        with open(file_path, 'wb') as file:

            bytes_stream = io.BytesIO(self.data)
            while True:

                chunk = bytes_stream.read(CHUNK_SIZE)

                if not chunk:
                    del chunk
                    break

                file.write(chunk)

            bytes_stream.close()

        self.write(json.dumps({"file_uuid": filename}))
        return self.set_status(status_code=200)
