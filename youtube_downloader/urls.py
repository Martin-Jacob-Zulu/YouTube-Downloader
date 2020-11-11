from django.urls import path
from .views import home_view, yt_download, download_complete

urlpatterns = [
    path('', home_view, name="home"),
    path('download/', yt_download, name="download"),
    path('download_complete/<res>', download_complete, name="download_complete")
]