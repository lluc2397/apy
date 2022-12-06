import importlib
from inspect import getmembers, isfunction
from typing import Dict, List


class ViewsInspector:
    @classmethod
    def parse_view(cls, url: type) -> Dict:
        info = cls.get_route(url)
        print(url.callback)
        print(url.callback.view_class)
        return info


class UrlsInspector:
    @staticmethod
    def parse_base_url(main_urls_module: str) ->List:
        module = importlib.import_module(main_urls_module)
        return module.urlpatterns

    @staticmethod
    def get_route(url: type) -> Dict:
        return {"route": url.pattern._route}

    @classmethod
    def parse_callback(cls, url: type) -> Dict:
        # Parse the view
        info = cls.get_route(url)
        # print(url.callback)
        # print(url.callback.view_class)
        return info

    @classmethod
    def parse_urlpattern(cls, urlpattern_module: type) -> Dict:
        return cls.scrap_urlpattern_list(urlpattern_module.urlconf_name.urlpatterns)

    @classmethod
    def parse_url_module(cls, url_module: type) -> Dict:
        # urlconf_name is the module of the url. Parsing that give sub urls
        if hasattr(url_module, "urlconf_name"):
            parsed_info = cls.parse_urlpattern(url_module)
        else:
            parsed_info = cls.parse_callback(url_module)
        return parsed_info

    @classmethod
    def scrap_urlpattern_list(cls, list_urls: List) -> Dict:
        info = {}
        for index, url in enumerate(list_urls):
            info[f"level_{index}"] = cls.parse_url_module(url)
        return info
