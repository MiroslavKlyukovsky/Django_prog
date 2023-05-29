from django.urls import path
from fitness_service.views import ClubListView, ClubDetailView, AbonementCreateView, AbonementListView
from . import views

urlpatterns = [
    path("", ClubListView.as_view(), name="club-list"),
    path("abonements/", AbonementListView.as_view(), name="abonement-list"),
    path("abonements/create/", AbonementCreateView.as_view(), name="abonement-create-super"),

    path("clubs/<int:pk>/", ClubDetailView.as_view(), name="club-detail"),
    path("clubs/<int:pk>/abonement/create/", AbonementCreateView.as_view(), name="abonement-create")
]

app_name = "fitness_service"
