from django.shortcuts import render

# Create your views here.


tasks = ["foo", "bar", "baz"]


def index(request):
    return render(request, "simple_app/index.html")

def alternative(request):
    return render(request, "simple_app/index2.html")