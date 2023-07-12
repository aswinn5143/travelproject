from django.shortcuts import render

from flying.models import Travelbuddy


# Create your views here.
def demo(request):
    obj = Travelbuddy.objects.all()
    return render(request, "index.html", {'result': obj})
