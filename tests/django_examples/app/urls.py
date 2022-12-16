from django.urls import path

from .views import APITestView

urlpatterns = [
    path(
        "some-url/<int:object_pk>/",
        APITestView.as_view(),
        name="object-detail",
    ),
]
