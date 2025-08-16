from django.urls import path
from . import views

urlpatterns = [
    path('submit-emoji/', views.submit_emoji, name="submit_emoji"),
    path('get-emojis/', views.get_all_emojis, name='get_all_emojis'),
]


