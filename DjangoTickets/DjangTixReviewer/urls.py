from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path("user/list", views.UserList.as_view(), name="userlist"),
  path("tickets/list", views.TicketList.as_view(), name="ticketlist")
]