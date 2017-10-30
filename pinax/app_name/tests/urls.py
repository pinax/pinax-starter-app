from django.conf.urls import include, url


urlpatterns = [
    url(r"^", include("pinax.{{ app_name }}.urls")),
]
