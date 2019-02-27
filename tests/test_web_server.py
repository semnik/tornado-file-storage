import json
import unittest
import re
import uuid

from tornado.testing import AsyncHTTPTestCase
import main


class TestRequest(AsyncHTTPTestCase):

    def setUp(self):
        self.file_uuid = 'cd85d86f-a36b-455d-bfa4-9cd73d0d42ef'
        super(TestRequest, self).setUp()

    def get_app(self):
        return main.get_app()

    # TODO : add test storage deleting , if exist folder delete and recreate
    def test_upload(self):
        resp = self.fetch('http://localhost:9999/upload', method="POST", body=b'test')

        body = resp.body
        expected_dict_json = json.loads(body)

        uuid_regex = re.compile('^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z')
        match = uuid_regex.match(expected_dict_json['file_uuid'])

        self.file_uuid = expected_dict_json['file_uuid']
        self.assertEqual(resp.code, 200)
        self.assertTrue(bool(match))

    def test_check(self):
        self.test_upload()
        resp = self.fetch('http://localhost:9999/check/{}'.format(self.file_uuid))

        self.assertEqual(resp.code, 200)

    def test_download(self):
        self.test_upload()
        resp = self.fetch('http://localhost:9999/download/{}'.format(self.file_uuid))

        self.assertEqual(resp.code, 200)
        self.assertEqual(resp.body, b'test')

    def test_download_204(self):
        filename = str(uuid.uuid4())
        resp = self.fetch('http://localhost:9999/download/{}'.format(filename))
        self.assertEqual(resp.code, 204)


if __name__ == '__main__':
    unittest.main()
