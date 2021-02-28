from django.contrib import admin
from .models import User, Agent, Lead, ProfitabilityCalculator, UserProfile, Category


admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Lead)
admin.site.register(ProfitabilityCalculator)
admin.site.register(UserProfile)
admin.site.register(Category)