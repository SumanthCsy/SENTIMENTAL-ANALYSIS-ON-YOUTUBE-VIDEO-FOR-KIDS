from django.contrib import admin
from .models import UserdetailsModel

# Register your models here.

@admin.register(UserdetailsModel)
class UserdetailsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_email', 'user_city', 'user_status', 'datetime_created')
    list_filter = ('user_status', 'user_city')
    search_fields = ('user_name', 'user_email')
