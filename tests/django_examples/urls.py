from django.urls import include, path

urlpatterns = [
    path("api/", include("tests.django_examples.app.urls")),
    path("api-2/", include("tests.django_examples.app.more_urls")),
]
