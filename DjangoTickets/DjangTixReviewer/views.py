from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
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

class TicketCreate(CreateView):
    model = Tickets
    template_name = "DjangTixReviewer/Ticket_Create_form.html"
    fields = ["Owner","Name","Description","CreateDate","DueDate","IsClosed","RelevantUsers"]
class TicketUpdate(UpdateView):
    model = Tickets
    template_name = "DjangTixReviewer/Ticket_Update_form.html"
    fields = ["Owner","Name","Description","CreateDate","DueDate","IsClosed","RelevantUsers"]