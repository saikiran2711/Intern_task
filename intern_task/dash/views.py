
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages


def func(x, n): 
    """ recursive function to calculate 1/x^i"""     
    if n == 1:
        return 1 / x
    else:
        return 1 / (x ** n) + func(x, n - 1)


@login_required()
def home(request):
    username = request.user.username
    return render(request, 'dash/home.html', {'username': username})


@login_required()
def calculate(request):
    if request.method == 'POST':
        
        if((request.POST.get('x_id') == "") or (request.POST.get('n_id') == "")):
            
            messages.error(request,'Please enter both X and N values !!!')
            return redirect('calc')
        x = int(request.POST.get('x_id'))
        n = int(request.POST.get('n_id'))
        
        res = func(x, n)
        return render(request, 'dash/calc.html', {'res': res})
    return render(request, 'dash/calc.html')
