from django.contrib import admin
from .models import CustomUser, Agent, Lead, ProfitabilityCalculator


admin.site.register(CustomUser)
admin.site.register(Agent)
admin.site.register(Lead)
admin.site.register(ProfitabilityCalculator)