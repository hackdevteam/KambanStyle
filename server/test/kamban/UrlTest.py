import unittest

from server.kamban.Url import Url


FILE_SCHEME = Url.SCHEME_FILE
LOCAL_DOMAIN = "localhost"
RESOURCES = "resources/foo.txt"


class UrlTest(unittest.TestCase):
    def test_url_for_file(self):
        self.assertEquals("file" + ":" + LOCAL_DOMAIN + "/" + RESOURCES, Url(FILE_SCHEME, LOCAL_DOMAIN, RESOURCES).get_url())

    def test_scheme_for_file(self):
        self.assertEquals(FILE_SCHEME, Url(FILE_SCHEME, LOCAL_DOMAIN, RESOURCES).get_scheme())

    def test_domain_for_file(self):
        self.assertEquals(LOCAL_DOMAIN, Url(FILE_SCHEME, LOCAL_DOMAIN, RESOURCES).get_domain())

    def test_resource_for_file(self):
        self.assertEquals(RESOURCES, Url(FILE_SCHEME, LOCAL_DOMAIN, RESOURCES).get_resource())

    def test_port_is_empty_if_not_passed_in_constructor(self):
        self.assertEquals("", Url(FILE_SCHEME, LOCAL_DOMAIN, RESOURCES).get_port())