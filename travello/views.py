from django.shortcuts import render
from django.http import HttpResponse
from . models import destination

# Create your views here.
def index(request):
    dests = destination.objects.all()

    return render(request,'index.html',{'dests':dests})


# def index(request):

#     dest1 = destination()
#     dest1.name = 'Mumbai'
#     dest1.desc = 'The city that never sleepssssss!'
#     dest1.price = 700
#     dest1.image = 'destination_1.jpg'
#     dest1.offer = False

#     dest2 = destination()
#     dest2.name = 'Malaysia'
#     dest2.desc = 'The city that never DIE!'
#     dest2.price = 600
#     dest2.image = 'destination_2.jpg'
#     dest2.offer = True

#     dest3 = destination()
#     dest3.name = 'Singapore'
#     dest3.desc = 'The city that GAMBLES!'
#     dest3.price = 500
#     dest3.image = 'destination_3.jpg'
#     dest3.offer = False

#     dests = [dest1, dest2, dest3]

#     return render(request,'index.html', {'dests': dests})
