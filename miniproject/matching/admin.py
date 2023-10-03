from django.contrib import admin
from .models import MatchingPost


# Register your models here.
class MatchingPostAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(MatchingPost, MatchingPostAdmin)