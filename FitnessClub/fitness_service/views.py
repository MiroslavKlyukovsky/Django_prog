from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from fitness_service.models import Club, Abonement, Day
from django.http import HttpResponse


class ClubListView(generic.ListView):
    model = Club


class ClubDetailView(generic.DetailView):
    model = Club

    def get_context_data(self, **kwargs):               #
        context = super().get_context_data(**kwargs)

        abonements = Abonement.objects.filter(user=self.request.user, club=self.object).all()
        day_list = []
        for abonement in abonements:
            day_list += abonement.days.all()
        days = Day.objects.all()
        context['days'] = days
        context['day_list'] = day_list
        return context


class AbonementListView(generic.ListView):
    model = Abonement


class AbonementCreateView(generic.CreateView):
    model = Abonement
    fields = ["club", "days"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        # if self.kwargs.get("pk") is not None:
        #     form.instance.club = get_object_or_404(Club, pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        if self.kwargs.get("pk") is not None:
            return reverse_lazy("fitness_service:club-detail", args=[self.kwargs["pk"]])
        else:
            return reverse_lazy("fitness_service:abonement-list")

