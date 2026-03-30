from django.contrib import admin
from .models import VideoModel, FeedbackModel

# Register your models here.

@admin.register(VideoModel)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('vid_id', 'vid_url_id', 'vid_sentiment', 'datetime_searched', 'search_author')
    list_filter = ('vid_sentiment', 'datetime_searched')
    search_fields = ('vid_url_id', 'vid_sentiment')

@admin.register(FeedbackModel)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('feedback_id', 'reviewer', 'rating', 'sentiment', 'datetime_reviewed')
    list_filter = ('rating', 'sentiment', 'datetime_reviewed')
    search_fields = ('review', 'sentiment')
