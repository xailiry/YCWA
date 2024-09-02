from django.contrib import admin
from django.urls import path

from YCWA.views import create_entire, delete_all_entries, get_new_entries

urlpatterns = [
    path('', create_entire, name='create_entire'),
    path('delete/', delete_all_entries, name='delete_all_entries'),
    path('get-new-entries/', get_new_entries, name='get_new_entries'),
]
