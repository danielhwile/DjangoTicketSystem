from django.shortcuts import render
from .models import *
from django.views.generic import ListView
# Create your views here.
def home(request):
    context = {"name": "Daniel"}
    return render(request, "DjangTixReviewer/home.html", context)
class UserList(ListView):
  model = UserNames
  template_name = "DjangTixReviewer/user_list.html"

class TicketList(ListView):
  model = Tickets
  template_name = "DjangTixReviewer/ticket_list.html"