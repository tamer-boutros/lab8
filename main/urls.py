from django.urls import path
from . import views

app_name = "main"   

urlpatterns = [
    path("create/", views.create, name="create"),
    path("display/", views.display, name="display"),
    path("edit/<str:name>", views.edit, name="edit"),
    path("delete/<str:name>/", views.delete, name="delete"),
    path("display/name=<str:name>", views.search_by_name, name="search_by_name"),
    path("display/tel=<str:tel>", views.search_by_phone, name="search_by_phone"),
    path("display/prof=<str:profession>", views.search_by_profession, name="search_by_profession"),
    path("display/<str:name1>/<str:name2>", views.compare_fields, name="compare_fields"),
    path("display/name/", views.bynamepage, name="bynamepage"),
    path("display/tel/", views.bytelpage, name="bytelpage"),
    path("display/compare/", views.comparepage, name="comparepage"),
    path("display/prof/", views.byprofpage, name="byprofpage"),
    path("", views.main, name="main"),
    path("display/sorted/", views.display_sorted, name="display_sorted"),

]