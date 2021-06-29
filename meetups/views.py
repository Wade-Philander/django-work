from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    meetups = [
        {'title': 'A First Meetup', 
        'location':'New York', 
        'slug': 'a-first-meetup'},

        {'title': 'A Second Meetup', 
        'location':'Paris', 
        'slug': 'a-second-meetup'}
    ]
    return render(request,'index.html',{
        'show_meetups': True,
        'meetups': meetups
    })

def meetup_details(request, meetup_slug):
    
    selected_meetups = {'title':'A First Meetup', 'description':'This is our first meetup!'}
    
    return render(request, 'meetup-detail.html',{
        'meetup_title': selected_meetups['title'],
        'meetup_description': selected_meetups['description'],
    })