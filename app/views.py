from django.shortcuts import render
def func1(request):
    d={'name':'harsha','age':20}
    return render(request,'html.htm',context=d)
