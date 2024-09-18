# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.

# # def app(request):
# #     x='hello to all..'
# #     return HttpResponse(x)

# def tem(request):
#     return render(request,'home.html')

from django.shortcuts import render

# Create your views here.

def homeApp(request):
    return render(request,'home.html')