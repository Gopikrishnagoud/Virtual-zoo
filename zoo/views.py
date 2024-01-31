from django.shortcuts import HttpResponse,render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def page(request):
     return render (request,'zoo/main_page.html')
@csrf_exempt
def Register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        emailId=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if User.objects.filter(username=emailId).exists():
             return HttpResponse("username has been already registered!!")
        
        if User.objects.filter(email=emailId).exists():
             return HttpResponse("this email id has been already used!!")
        
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(username,emailId,pass1)
            my_user.save()
            return redirect('login')
        
    return render (request,'zoo/register.html')
@csrf_exempt
def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
     
     
        if user is not None:
            login(request,user)
            return redirect('direct')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'zoo/login.html')

def  Direct(request):
     return render(request,'zoo/direction.html')
def page1(request):
    return render(request, 'zoo/wild.html')
def mammals(request):
    return render(request, 'zoo/mammals.html')
def deers(request):
     return render(request,'zoo/deers.html') 
def snakes(request):
     return render(request,'zoo/snakes.html')
def crocodiles(request):
     return render(request,'zoo/crocodiles.html')
def turtules(request):
     return render(request,'zoo/turtules.html')
def birds(request):
     return render(request,'zoo/birds.html')
def aquatic(request):
     return render(request,'zoo/aquatic.html')
def bears(request):
     return render(request,'zoo/bear.html')
def mammalia(request):
     return render(request,'zoo/mammalia.html')
def lizards(request):
     return render(request,'zoo/lizards.html')
def Extinct_Animals(request):
     return render(request,'zoo/Extinct_Animals.html')
def mammalias(request):
     return render(request,'zoo/mammalia.html')
def hybrid(request):
     return render(request,'zoo/hybrid.html')
def horse(request):
     return render(request,'zoo/hores.html')
def logout(request):
     return render(request,'zoo/logout.html')
