from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        print('SUBMITTED reg')
        return redirect('register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        #login user
        return redirect('index.html')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    return redirect(request,'index.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')