from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import ResultsView, InputFormView
# from ggrl13 import settings

app_name = 'simple'


urlpatterns = [
    path("form/", InputFormView.as_view(), name="form"),
    path("results/", ResultsView.as_view(), name="results"),]
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)