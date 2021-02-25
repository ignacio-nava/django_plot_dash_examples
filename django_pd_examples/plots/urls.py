from django.urls import path
from . import views

app_name = 'plots'
urlpatterns = [
    path('<slug:example>/', views.exampleDetailView, name='plot_detail')
]