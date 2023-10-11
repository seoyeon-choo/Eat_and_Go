# from django.contrib import admin
# from .models import *

# # Register your models here.
# admin.site.register(Gift, Code)


from django.contrib import admin
from .models import Gift, Code

# Gift 모델을 Admin 페이지에서 관리할 수 있도록 등록
@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('giver', 'taker', 'check', 'message', 'create_dt', 'update_dt')
    list_filter = ('check', 'create_dt')
    search_fields = ('giver__username', 'taker', 'message')
    date_hierarchy = 'create_dt'

# Code 모델을 Admin 페이지에서 관리할 수 있도록 등록
@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'message', 'phone_number')
    list_filter = ('quantity',)
    search_fields = ('phone_number', 'message')

# 기타 설정 및 커스터마이징이 필요한 경우 추가할 수 있습니다.
