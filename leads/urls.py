
from django.urls import path, include
from .views import AssignedAgentView,     LeadListView,LeadDetailView,    LeadCreateView, LeadUpdateView, LeadDeleteView, CategoryListView, CategoryDetailView,LeadCategotyUpdateView
    
app_name='leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('<int:pk>/assign-agent/', AssignedAgentView.as_view(), name='assign-agent'),
    path('categories/',CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>',CategoryDetailView.as_view(), name='category-detail'),
    path('<int:pk>/category/', LeadCategotyUpdateView.as_view(), name='assign-category'), 

]
