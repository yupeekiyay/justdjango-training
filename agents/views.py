from django.core.mail import send_mail
from django.shortcuts import render, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import OrganizerAndLoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
import random
class AgentListView(OrganizerAndLoginRequiredMixin,ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization = organization)
    



class AgentCreateView(OrganizerAndLoginRequiredMixin, CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent-list')

    def form_valid(self,form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organizer = False
        user.set_password(f"random.randint(0,1000000)")
        user.save()
        Agent.objects.create(user=user,
        organization = self.request.user.userprofile)
        send_mail(
            subject="You are invited to be an agent",
            message="You were added as an agent on FlexaCRM, please come login to start working",
            from_email = "test@test.com",
            recipient_list=["admin@test.com",]


        )
        # agent.organization = self.request.user.userprofile
        # agent.save()

        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(OrganizerAndLoginRequiredMixin, DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"
    
    
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization = organization)

class AgentUpdateView(OrganizerAndLoginRequiredMixin, UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent-list')

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization = organization)

class AgentDeleteView(OrganizerAndLoginRequiredMixin, DeleteView):
    template_name = "agents/agent_delete.html"

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization = organization)
     
    def get_success_url(self):
        return reverse('agents:agent-list')