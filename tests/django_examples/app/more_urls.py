from django.urls import path

from .more_views import APISub2TestView, APISub3TestView, APISubTestView

urlpatterns = [
    path(
        "suburl-2/",
        APISubTestView.as_view(),
        name="object-2-detail",
    ),
    path(
        "suburl-3/",
        APISub2TestView.as_view(),
        name="object-3-detail",
    ),
    path(
        "suburl-4/",
        APISub3TestView.as_view(),
        name="object-4-detail",
    ),
]
