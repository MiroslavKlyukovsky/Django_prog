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
