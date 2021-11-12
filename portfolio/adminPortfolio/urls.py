from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from adminPortfolio.views import AccueilPortfolio

urlpatterns = [
                  path('', AccueilPortfolio.as_view(), name="infoUser"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
