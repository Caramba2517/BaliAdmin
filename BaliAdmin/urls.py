from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from appart.views import image_view

urlpatterns = [
    path('', RedirectView.as_view(url='/admin/', permanent=True)),
    path('admin/', admin.site.urls),
    path('images/<path:path>', image_view, name='image_view')
]
