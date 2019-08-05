from django.urls import path, include
from oscarapi.app import application as api


urlpatterns = [
    path('oscarapi/', api.urls),
]
