import importlib
from unittest.mock import patch

from apy import apy


class TestUrlsInspector:
    def test_parse_base_url(self):
        list_urls = apy.UrlsInspector.parse_base_url("tests.django_examples.urls")
        assert isinstance(list_urls, list)

    @patch("apy.apy.UrlsInspector.parse_urlpattern")
    @patch("apy.apy.UrlsInspector.parse_callback")
    def test_parse_url_module(self, mock_parse_callback, mock_parse_urlpattern):
        url_pattern_module = importlib.import_module("tests.django_examples.urls").urlpatterns[0]
        url_callback = url_pattern_module.urlconf_name.urlpatterns[0]
        apy.UrlsInspector.parse_url_module(url_pattern_module)
        mock_parse_urlpattern.assert_called_once_with(url_pattern_module)
        apy.UrlsInspector.parse_url_module(url_callback)
        mock_parse_callback.assert_called_once_with(url_callback)

    def test_parse_urlpattern(self):
        module_urlpattern = apy.UrlsInspector.parse_base_url("tests.django_examples.urls")[0]
        assert {
                   'level_0': {
                       'route': 'some-url/<int:object_pk>/'
                   }
               } == apy.UrlsInspector.parse_urlpattern(module_urlpattern)

    def test_scrap_urlpattern_list(self):
        modules_urlpattern = apy.UrlsInspector.parse_base_url("tests.django_examples.urls")
        assert {
            'level_0': {
                'level_0': {
                    'route': 'some-url/<int:object_pk>/'}
                }, 'level_1': {'level_0': {'route': 'suburl-2/'}, 'level_1': {'route': 'suburl-3/'}, 'level_2': {'route': 'suburl-4/'},
            },
        } == apy.UrlsInspector.scrap_urlpattern_list(modules_urlpattern)


