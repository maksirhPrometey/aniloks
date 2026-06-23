from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

urlpatterns = [
    path("healthz/", lambda request: HttpResponse("ok", content_type="text/plain")),
    path("admin/", admin.site.urls),
    path("", include("src.core.urls")),
    path("catalog/", include("src.catalog.urls")),
    path("contacts/", include("src.contacts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
