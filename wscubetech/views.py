from django.http import HttpResponse
from django.shortcuts import render
from featured_book.models import featured_book

def home(request):
    books = featured_book.objects.all()
    data = {
        'featured_book': books,
    }
    
    
    return render(request, 'index.html', data)


def aboutUS(request):
    return render(request,'about.html')

def course(request):
    return HttpResponse("<h1>Course</h1><p>We are a leading tech education platform.</p>")

def products(request):
    return render(request, 'products.html')



def index(request):
    # data= {
    #     'name': 'WS Cubetech',
    #     'course': 'Django Full Stack Development',
    #     'duration': '3 Months',
    #     'location': ['Online','Noida','Delhi', 'Gurgaon', 'Bangalore'],
    #     'instructor': 'John Doe',
    #     'description': 'Learn Django from scratch with hands-on projects.',
    #     'contact_email': 'abhi620548@gmail.com',
    # }
    return render(request,'index.html')



