# from django.test import TestCase, Client
# from fitness_service.models import Club, Day, Abonement
# from django.urls import reverse
#
#
# CLUB_URL = reverse("fitness_service:club-list")
#
# class PublicClubTests(TestCase):
#     def setUp(self) -> None:
#         self.client = Client()
#
#     def test_retrieve_clubs(self):
#         Club.objects.create(location="somee location")
#         Club.objects.create(location="some location")
#
#         response = self.client.get(CLUB_URL)
#         clubs = Club.objects.all()
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(list(response.context["club_list"]), list(clubs))
#         self.assertTemplateUsed(response, "fitness_service/club_list.html")
#
# class PublicAbonementTests(TestCase):
#     def setUp(self) -> None:
#         self.client = Client()
#
#     def test_create_abonement(self):
#         club = Club.objects.create(location="some location")
#         day = Day.objects.create(name="Friday", exercise="Box")
#         form_data = {"club": club, "day": day}
#
#         response = self.client.post(reverse("fitness_service:abonement-create", kwargs={"pk": club.pk}), data=form_data)
#
#         print(Abonement.objects.first())
#         self.assertNotEqual(response.status_code, 200)
#         self.assertFalse(Abonement.objects.filter(club=club).exists())
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Club, Abonement, Day


class ClubListViewTest(TestCase):
    def setUp(self):
        self.url = reverse("fitness_service:club-list")

    def test_club_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed


class ClubDetailViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username="testuser")
        self.club = Club.objects.create(location="Test Location")
        self.abonement = Abonement.objects.create(user=self.user)
        self.abonement.club.add(self.club)
        self.day = Day.objects.create(name="Monday")
        self.abonement.days.add(self.day)
        self.url = reverse("fitness_service:club-detail", args=[self.club.pk])

    def test_club_detail_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed


class AbonementListViewTest(TestCase):
    def setUp(self):
        self.url = reverse("fitness_service:abonement-list")

    def test_abonement_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed


class AbonementCreateViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username="testuser")
        self.club = Club.objects.create(location="Test Location")
        self.day = Day.objects.create(name="Monday")
        self.url = reverse("fitness_service:abonement-create",kwargs={"pk":self.club.pk})

    def test_abonement_create_view(self):
        self.client.force_login(self.user)
        response = self.client.post(self.url, data={"club": self.club.pk, "days": [self.day.pk]})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Abonement.objects.count(), 1)
        # Add more assertions as needed
