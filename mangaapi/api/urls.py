from django.urls import path
from .views import PopularMangasView, TopTenMangasView, MostViewedMangasView, MangaView

urlpatterns = [
    path("popular/", PopularMangasView.as_view(), name="popular"),
    path("top-ten/", TopTenMangasView.as_view(), name="top-ten"),
    path("most-viewed/<str:chart>/", MostViewedMangasView.as_view(), name="most-viewed"),
    path("manga/<slug:slug>/", MangaView.as_view(), name="manga")
]