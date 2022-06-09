
from django.contrib import admin
from django.urls import include, path

# urls
urlpatterns = [
    path('', include('aktu_api.urls')),
    path('admin/', admin.site.urls),
]