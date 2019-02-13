import json
import logging
import os
import uuid
import tornado.web
from tornado import iostream, gen
from tornado.ioloop import IOLoop


class FileHandler(tornado.web.RequestHandler):

    def initialize(self, upload_dir):

        self.upload_dir = upload_dir

    async def put(self):

        self.set_header('Content-Type', 'application/json')
        filename = str(uuid.uuid4())

        binary_data = self.request.body

        filepath = os.path.join(self.upload_dir, filename)
        with open(filepath, 'wb') as file:
            file.write(binary_data)
            await gen.sleep(0.000000001)

        logging.info("file uploaded , saved as %s",
                     filename)
        self.set_status(status_code=200)
        self.write(json.dumps({"file_uuid": filename}))

    async def get(self):

        file_uuid = self.request.headers.get('file_uuid')

        if file_uuid is None:
            self.send_error(400, message="file_uuid ")

        file_path = os.path.join(self.upload_dir, file_uuid)
        file_exists = os.path.isfile(file_path)

        if file_exists:

            chunk_size = 1024 * 1024 * 1  # 1 MiB
            self.set_header('Content-Type', 'application/octet-stream')
            self.set_header('Content-Disposition', 'attachment; filename=' + file_uuid)
            with open(file_path, 'rb') as f:
                while True:

                    deadline = IOLoop.current().time() + 0.1  # set minimum chunk_size handle time

                    chunk = f.read(chunk_size)
                    if not chunk:
                        break
                    try:
                        self.write(chunk)
                        await self.flush()
                    except iostream.StreamClosedError:
                        break
                    finally:
                        del chunk
                        # pause the coroutine so other handlers can run
                        await gen.sleep(deadline - IOLoop.current().time())  # 1 nanosecond

            self.set_status(status_code=200)
        else:
            self.set_status(status_code=204)

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
