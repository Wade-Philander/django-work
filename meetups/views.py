from django.shortcuts import render

from .models import Meetup

# from django.http import HttpResponse

# Create your views here.

 # BELOW IS MOCK DATA 
    # meetup = [
    #     {'title': 'A First Meetup', 
    #     'location':'New York', 
    #     'slug': 'a-first-meetup'},

    #     {'title': 'A Second Meetup', 
    #     'location':'Paris', 
    #     'slug': 'a-second-meetup'}
    # ]
    # return render(request,'meetups/index.html',{
    #     'show_meetups': True,
    #     'meetups': meetups
    # })

def index(request):
    meetups = Meetup.objects.all()

    return render(request,'meetups/index.html',{
        'meetups': meetups
    })

def meetup_details(request, meetup_slug):
    
    selected_meetups = {'title':'A First Meetup', 'description':'This is our first meetup!'}
    
    return render(request, 'meetups/meetup-detail.html',{
        'meetup_title': selected_meetups.title,
        'meetup_description': selected_meetups.description
    })