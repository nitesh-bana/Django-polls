

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("poll/", include("poll.urls")),
    path("admin/", admin.site.urls),
   
]
