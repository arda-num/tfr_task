from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='api-root'),
    path("search", views.search.as_view(), name="api-search"),
    path("dbinfo", views.getDatabaseInfo, name="db-info"),
    path("cleardb", views.cleanDatabase, name="db-clear")
]