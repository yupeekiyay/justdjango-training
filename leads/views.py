from typing import List
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lead, Agent
from .forms import LeadModelForm


# class LandingPageView(TemplateView):
#     template_name = 'landing_page2.html'


def landing_page(request):
    return render(request, 'landing_page2.html')


class LeadListView(ListView):
    template_name = "leads/leads_list.html"
    queryset = Lead.objects.all()
    context_object_name = 'leads'


class LeadDetailView(DetailView):
    template_name = "leads/leads_detail.html"
    queryset = Lead.objects.all()
    context_object_name = 'lead'



class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse('leads:lead-list')


class LeadCreateView(CreateView):
    template_name= "leads/lead_create.html"
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse('leads:lead-list')



class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')


