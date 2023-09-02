from django.urls import path
from .views import PopularMangasView

urlpatterns = [
    path("popular/", PopularMangasView.as_view(), name="popular")
]