from django.conf.urls import include


urlpatterns = [
    (r"^", include("pinax.{{ app_name }}.urls")),
]
