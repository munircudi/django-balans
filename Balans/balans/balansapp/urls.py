from django.urls import path
from . import views


urlpatterns=[
    path("", views.index, name="ana-sayfa"),
    path("markalar",views.balansapp, name="markalar"),
    path("markalar/<slug:name>", views.balansapp_details, name="markalar-details"),
    path("about", views.about, name="about")



]

