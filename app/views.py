from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def form(request):
    if request.method == "post":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        file = None
        if request.FILES:
            file = request.FILES['profile_pic']
            fs = FileSystemStorage()
            saved_file = fs.save(file.name,file)
            file_url = fs.url(saved_file)
        return HTTPResponse("<h1>FILE SUBMITTED {} <br> {} <br> <img src='{}'></h1>".format(fname,lname,file_url))



    return render(request, 'form.html')