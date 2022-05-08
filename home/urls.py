from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('questions/', views.QuestionListView.as_view(), name='questions'),
    path('questions/create/', views.QuestionCreateView.as_view(), name='create_question'),
    path('questions/update/<int:pk>/', views.QuestionUpdateView.as_view(), name='update_question'),
    path('questions/delete/<int:pk>/', views.QuestionDeleteView.as_view(), name='delete_question'),
]
