import unittest
import os
import sys
import requests
sys.path.append(os.getcwd())

from book_information import BookRequest

class TestConfigureRequest(unittest.TestCase):
    def test_configure_url(self):
        input = "-f 9780521825146"
        cite = BookRequest(input)

        cite.configureBookUrl()

        self.assertEqual(cite.request_url, "https://www.googleapis.com/books/v1/volumes?q=isbn:9780521825146")

    def test_request(self):
        input = "-f 9780521825146"

        cite = BookRequest(input)

        cite.requestBookInformation()
        self.assertEqual(cite.response.status_code, 200)