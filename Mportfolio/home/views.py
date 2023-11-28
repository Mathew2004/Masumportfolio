from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Home,Portfolio,Contact,About
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    res = Home.objects.all().values()
    write = res[0]['typewrite']
    #Portfolio
    portfolio = Portfolio.objects.all().order_by('id')[:3]



    return render(request,'home/index.html',{
        'homeRes': res,
        'typewrite': write,
        'portfolio':portfolio,
    })


def about(request):
    about = About.objects.all()
    
    return render(request,'home/about.html',{
        'about':about
    })

def portfolio(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'home/portfolio.html',{
        'portfolio':portfolio,
    })


def contact(request):
    msg = Contact.objects.all()
    if(request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']
        phn = request.POST['phn']
        msg = request.POST['msg']

        Contact(name=name, email=email, phn=phn, msg=msg).save()
        messages.success(request, 'Message Has been Sent Successfully!')
        return redirect('/contact/')


    return render(request,'home/contact.html',{
        'message':msg
    })



def dashboard(request):
    about = Home.objects.all()
    msg = Contact.objects.all()

    if(request.method == 'POST'):
        name = request.POST['name']
        des = request.POST['description']
        typewrite = request.POST['typewrite']

        Home.objects.update_or_create(id=1,
            defaults={
                'name':name,
                'des':des,
                'typewrite':typewrite,
                

            })
        messages.success(request, 'Your Personal Information has been Updated!')
        return redirect("/dashboard")
       

    return render(request,"admin/home.html",{
        'about':about,
        'contact':msg
    })

def Messages(request):
    msg = Contact.objects.all()

    return render(request,'admin/messages.html',{
        'contact':msg,
    })

def handlelogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect("/dashboard/")
        else:
            messages.warning(request, "Invalid credentials! Please try again")
            return redirect("/login")

    
    return render(request,'admin/login.html')

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

def adminAbout(request):
    

    return render(request,"admin/about.html")


def uploadPic(request):

    if(request.method == "POST"):
        img = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_url = fs.url(filename)

        Home.objects.update_or_create(id=1,
            defaults={
                'img':filename,
            })
        
        return redirect('/dashboard/about')

    return HttpResponse("ERROR")

def portPic(request,id):

    if(request.method == "POST"):
        img = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_url = fs.url(filename)

        Portfolio.objects.update_or_create(id=id,
            defaults={
                'img':filename,
            })
        messages.success(request, 'Image has been Updated!')
        return redirect('/dashboard/portfolio')
        

    return HttpResponse("ERROR")

def AdminPortfolio(request):
    portfolio = Portfolio.objects.all()
    msg = Contact.objects.all()
    
    if(request.method == 'POST'):
        title = request.POST['name']
        des = request.POST['description']
        view = request.POST['view']
        img = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_url = fs.url(filename)

        portfolio = Portfolio(name=title, description=des,img=img, view=view)
        portfolio.save()
        messages.success(request, 'Your Personal Information has been Updated!')
        return redirect('/dashboard/portfolio')

    return render(request,"admin/portfolio.html",{
        'portfolio':portfolio,
        'contact': msg,
    })

def editPortfolio(request,id):
    portfolio = Portfolio.objects.filter(id=id)
    if(request.method == 'POST'):
        title = request.POST['title']
        des = request.POST['description']
        view = request.POST['view']

        Portfolio.objects.update_or_create(id=id,
            defaults={
                'name':title,
                'description':des,
                'view': view,

            })
        messages.success(request, 'Portfolio has been Updated!')
        return redirect('/dashboard/portfolio')


def dltPortfolio(request,id):
   
    Portfolio.objects.filter(id=id).delete()
    messages.success(request, 'Your Profile Has been Deleted')
    return redirect('/dashboard/portfolio')          

