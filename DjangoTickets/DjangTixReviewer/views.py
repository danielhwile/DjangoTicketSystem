from django.shortcuts import render
# Create your views here.
def home(request):
    context = {"name": "Daniel"}
    return render(request, "DjangTixReviewer/home.html", context)