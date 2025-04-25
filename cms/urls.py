from django.urls import path
from . import views

urlpatterns = [
    path('', views.story_list, name='story_list'),
    path('play/<int:story_id>/', views.story_start, name='story_start'),
    path('chapter/<int:chapter_id>/', views.show_chapter, name='show_chapter'),
]

