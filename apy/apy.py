import importlib
from inspect import getmembers, isfunction
from typing import Any, Dict, List


class ViewsInspector:
    @classmethod
    def parse_view(cls, url: type) -> Dict:
        info = cls.get_route(url)
        print(url.callback)
        print(url.callback.view_class)
        return info


class UrlsInspector:
    @staticmethod
    def get_base_urlpattern(main_urls_module: str) -> List:
        module = importlib.import_module(main_urls_module)
        return module.urlpatterns

    @staticmethod
    def check_includes_more_urls(url_module: type) -> bool:
        return hasattr(url_module, "urlconf_name")

    @classmethod
    def get_urlpattern(cls, urlpattern_module: type) -> List[type]:
        return urlpattern_module.urlconf_name.urlpatterns

    @staticmethod
    def get_url_pattern_route(url: type) -> Dict[str, Any]:
        return {"route": url.pattern._route}

    @classmethod
    def parse_callback(cls, url: type) -> Dict:
        # A callback is a url for a view
        return cls.get_url_pattern_route(url)

    @classmethod
    def build_urlpatterns_structure(cls, urlpatterns: List) -> Dict:
        info = {}
        for index, url in enumerate(urlpatterns):
            info[f"level_{index}"] = cls.parse_url_module(url)
        return info

    @classmethod
    def parse_urlpatterns(cls, urlpattern_module: type) -> Dict:
        urlpattern = cls.get_urlpattern(urlpattern_module)
        return cls.build_urlpatterns_structure(urlpattern)

    @classmethod
    def parse_url_module(cls, url_module: type) -> Dict:
        # urlconf_name is the module of the url. Parsing that give sub urls
        if cls.check_includes_more_urls(url_module):
            parsed_info = cls.parse_urlpatterns(url_module)
        else:
            parsed_info = cls.parse_callback(url_module)
        return parsed_info
