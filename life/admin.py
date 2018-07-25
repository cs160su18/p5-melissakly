from django.contrib import admin
from life.models import *

# Register your models here.
class SpendingAdmin(admin.ModelAdmin):
  list_display = ('name', 'cost', 'description')

class EarningAdmin(admin.ModelAdmin):
  list_display = ('name', 'amount', 'description')
  
class AchievementAdmin(admin.ModelAdmin):
  list_display = ('week', 'goal', 'achieved')
    
admin.site.register(Spending, SpendingAdmin)
admin.site.register(Earning, EarningAdmin)
admin.site.register(Achievement, AchievementAdmin)
