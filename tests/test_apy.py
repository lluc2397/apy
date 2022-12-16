import importlib
from unittest.mock import patch

from apy.apy import UrlsInspector


class TestUrlsInspector:
    def test_get_base_urlpattern(self):
        list_urls = UrlsInspector.get_base_urlpattern("tests.django_examples.urls")
        assert isinstance(list_urls, list)
        assert (
            importlib.import_module("tests.django_examples.app.urls")
            == list_urls[0].urlconf_name
        )
        assert (
            importlib.import_module("tests.django_examples.app.more_urls")
            == list_urls[1].urlconf_name
        )

    def test_check_includes_more_urls(self):
        module = importlib.import_module(
            "tests.django_examples.app.more_urls"
        ).urlpatterns[0]
        assert UrlsInspector.check_includes_more_urls(module) is False
        module = importlib.import_module("tests.django_examples.urls").urlpatterns[0]
        assert UrlsInspector.check_includes_more_urls(module) is True

    def test_get_urlpattern(self):
        module = importlib.import_module("tests.django_examples.urls").urlpatterns[0]
        list_urls = UrlsInspector.get_urlpattern(module)
        assert isinstance(list_urls, list)

    def test_get_url_pattern_route(self):
        url = importlib.import_module("tests.django_examples.app.urls").urlpatterns[0]
        expected_result = {"route": "some-url/<int:object_pk>/"}
        assert expected_result == UrlsInspector.get_url_pattern_route(url)

    def test_parse_callback(self):
        url = importlib.import_module("tests.django_examples.app.urls").urlpatterns[0]
        expected_result = {"route": "some-url/<int:object_pk>/"}
        assert expected_result == UrlsInspector.parse_callback(url)

    @patch("apy.apy.UrlsInspector.parse_urlpatterns")
    @patch("apy.apy.UrlsInspector.parse_callback")
    def test_parse_url_module(self, mock_parse_callback, mock_parse_urlpattern):
        url_pattern_module = importlib.import_module(
            "tests.django_examples.urls"
        ).urlpatterns[0]
        url_callback = url_pattern_module.urlconf_name.urlpatterns[0]
        UrlsInspector.parse_url_module(url_pattern_module)
        mock_parse_urlpattern.assert_called_once_with(url_pattern_module)
        UrlsInspector.parse_url_module(url_callback)
        mock_parse_callback.assert_called_once_with(url_callback)

    def test_parse_urlpattern(self):
        module = importlib.import_module("tests.django_examples.urls")
        expected_result = {"level_0": {"route": "some-url/<int:object_pk>/"}}
        assert expected_result == UrlsInspector.parse_urlpatterns(module.urlpatterns[0])

    def test_build_urlpatterns_structure(self):
        module = importlib.import_module("tests.django_examples.urls")
        expected_result = {
            "level_0": {"level_0": {"route": "some-url/<int:object_pk>/"}},
            "level_1": {
                "level_0": {"route": "suburl-2/"},
                "level_1": {"route": "suburl-3/"},
                "level_2": {"route": "suburl-4/"},
            },
        }
        result = UrlsInspector.build_urlpatterns_structure(module.urlpatterns)
        print("*" * 100)
        print(result)
        assert expected_result == result
