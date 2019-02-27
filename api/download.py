import os

import tornado.web
from tornado import iostream, gen


class DownloadHandler(tornado.web.RequestHandler):

    def initialize(self, upload_dir):

        self.upload_dir = upload_dir

    async def get(self, file_uuid):

        CHUNK_SIZE = 1024 * 1024 * 1  # 1 MiB

        if file_uuid is None:
            self.send_error(400, message="file_uuid ")

        file_path = os.path.join(self.upload_dir, file_uuid)
        file_exists = os.path.isfile(file_path)

        if file_exists:

            self.set_header('Content-Type', 'application/octet-stream')
            self.set_header('Content-Disposition', 'attachment; filename=' + file_uuid)
            with open(file_path, 'rb') as f:
                while True:

                    chunk = f.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    try:
                        self.write(chunk)
                        # flush the current chunk to socket
                        await self.flush()
                    except iostream.StreamClosedError:
                        # this means the client has closed the connection
                        # so break the loop
                        break
                    finally:
                        # deleting the chunk is very important because
                        # if many clients are downloading files at the
                        # same time, the chunks in memory will keep
                        # increasing and will eat up the RAM
                        del chunk
                        # pause the coroutine so other handlers can run
                        await gen.sleep(0.000000001)  # 1 nanosecond

            self.set_status(status_code=200)
        else:
            self.set_status(status_code=204)
