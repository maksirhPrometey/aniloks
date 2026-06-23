from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path("submit/", views.contact_submit, name="submit"),
]
