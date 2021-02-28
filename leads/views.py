from typing import List
from django.db.models import query
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lead, Agent, Category
from .forms import LeadModelForm,CustomUserCreationForm, AssignAgentForm,LeadCategoryUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganizerAndLoginRequiredMixin
# class LandingPageView(TemplateView):
#     template_name = 'landing_page2.html'

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    
    form_class = CustomUserCreationForm
    def get_success_url(self):
        return reverse('login')

def landing_page(request):
    return render(request, 'landing_page2.html')


class LeadListView(LoginRequiredMixin,ListView):
    template_name = "leads/leads_list.html"
    
    context_object_name = 'leads'
    def get_queryset(self):
        user = self.request.user
        #initial queryset for the entire organization
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile, agent__isnull=False)
        else:

            queryset = Lead.objects.filter(organization=user.agent.organization)
            queryset= queryset.filter(agent__user = user)
            
        return queryset
    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        user=self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile, agent__isnull = True )
            context.update({
            "unassigned_leads": queryset
             })
        return context


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/leads_detail.html"
    context_object_name = 'lead'

    def get_queryset(self):
        user = self.request.user
        #initial queryset for the entire organization
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = queryset.filter(organization=user.agent.organization)
            queryset= queryset.filter(agent__user = user)
            
        return queryset
    

class LeadUpdateView(OrganizerAndLoginRequiredMixin, UpdateView):
    template_name = "leads/lead_update.html"
   
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse("leads:lead-detail", kwargs={"pk": self.get_object().id})
    def get_queryset(self):
        user = self.request.user
        #initial queryset for the entire organization
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        return queryset

class LeadCreateView(OrganizerAndLoginRequiredMixin, CreateView):
    template_name= "leads/lead_create.html"
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse('leads:lead-list')

    def form_valid(self, form):
        lead = form.save(commit = False)
        lead.organization = self.request.user.userprofile
        lead.save()
        send_mail(
            subject = " A lead has been created",
            message= " Go to a site to see a new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )

        return super(LeadCreateView, self).form_valid(form)


class LeadDeleteView(OrganizerAndLoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"

    def get_success_url(self):
        return reverse('leads:lead-list')

    def get_queryset(self):
        user = self.request.user
        #initial queryset for the entire organization
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        return queryset

class AssignedAgentView(OrganizerAndLoginRequiredMixin, generic.FormView):
    template_name = "leads/assign_agent.html"
    form_class = AssignAgentForm

    def get_form_kwargs(self, **kwargs):

        kwargs = super(AssignedAgentView,self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        }) 
        return kwargs

    def get_success_url(self):
        return reverse("leads:lead-list")
    
    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AssignedAgentView, self).form_valid(form)

class CategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/category_list.html"
    context_object_name = "category_list"

    def get_queryset(self):
        user = self.request.user
        #initial queryset for the entire organization
        if user.is_organizer:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:

            queryset = Category.objects.filter(organization=user.agent.organization)
            
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        user=self.request.user

        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:

            queryset = Lead.objects.filter(organization=user.agent.organization)
            

        context.update({
            "unassigned_lead_count": queryset.filter(category__isnull=True).count()
        })
        return context

class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/category_detail.html"
    context_object_name = "category"
    def get_queryset(self):
        user = self.request.user
        #initial queryset for the entire organization
        if user.is_organizer:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = queryset.filter(organization=user.agent.organization)
            
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)

        leads = self.get_object().leads.all()
        
        context.update({
            "leads":leads
        })

        return context

class LeadCategotyUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_category_update.html"
    form_class = LeadCategoryUpdateForm
    
    def get_queryset(self):
        user = self.request.user
        #initial queryset for the entire organization
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = queryset.filter(organization=user.agent.organization)
            queryset= queryset.filter(agent__user = user)
            
        return queryset
    
    def get_success_url(self):
        return reverse("leads:lead-detail", kwargs={"pk": self.get_object().id})