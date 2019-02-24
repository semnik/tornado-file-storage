import unittest

from tornado.testing import AsyncHTTPTestCase

import main


class TestWebServer(unittest.TestCase):
    def test_server(self):
        app = main.get_app()
        self.assertTrue(app)


class TestRequest(AsyncHTTPTestCase):
    def setUp(self):
        super(TestRequest, self).setUp()

    def get_app(self):
        return main.get_app()

    def test_upload(self):
        resp = self.fetch('http://localhost:9999/download/cd85d86f-a36b-455d-bfa4-9cd73d0d42ef', headers={
            'file_uuid': 'cd85d86f-a36b-455d-bfa4-9cd73d0d42ef'})
        cc = resp.body
        self.assertEqual(resp.code, 200)

    def test_check(self):
        resp = self.fetch('http://localhost:9999/check/cd85d86f-a36b-455d-bfa4-9cd73d0d42ef')
        cc = resp.body
        self.assertEqual(resp.code, 200)

    def test_download(self):
        # resp = self.fetch_json('http://localhost:9999/')
        resp = self.fetch('http://localhost:9999/download/cd85d86f-a36b-455d-bfa4-9cd73d0d42ef')
        cc = resp.body
        self.assertEqual(resp.code, 200)


if __name__ == '__main__':
    unittest.main()
