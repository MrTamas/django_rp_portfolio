from django.urls import path
from . import views
urlpatterns = [
	path("", views.angular_index, name="angular_index"),
]