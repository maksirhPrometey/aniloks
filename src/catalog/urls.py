from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("modal/category/<str:slug>/", views.category_modal, name="category_modal"),
]
