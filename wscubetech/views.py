from django.http import HttpResponse
from django.shortcuts import render
from featured_book.models import featured_book
from userform.models import UserForm


def home(request):
    books = featured_book.objects.all()
    data = {
        'featured_book': books,
    }
    
    
    return render(request, 'index.html', data)

def cart(request):
    return render(request,'cart.html')

def aboutUS(request):
    return render(request,'about.html')

def course(request):
    return HttpResponse("<h1>Course</h1><p>We are a leading tech education platform.</p>")

def products(request):
    return render(request, 'products.html')
def userfeedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        
        # Save the feedback to the database
        en = UserForm(name=name, email=email, message=feedback)
        en.save()
        
        # Optionally, you can redirect or render a success message
        return render(request, 'Userform.html', {'name': name})
    



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

def userform(request):
         try:
              if request.method == 'POST':
                  name = request.POST.get('name')
                  email = request.POST.get('email')
                  feedback = request.POST.get('feedback')
                  print(f"Name: {name}, Email: {email}, Phone: {feedback}")
         except:
                  pass        
         return render(request, 'Userform.html')  # Render the form template



