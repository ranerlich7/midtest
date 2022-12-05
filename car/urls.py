from django.urls import path
from . import views

app_name="car"
urlpatterns = [
    path('t', views.treatment, name="edit_treatment"),
    path('list', views.treatments, name="tlist"),
    path('charts', views.charts, name="charts")
]
