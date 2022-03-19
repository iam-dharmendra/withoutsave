from email import message
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.



# def index(request):   
#     if request.POST:
#         f = request.FILES.get('file1').read()
#         print(f)
#         f=str(f).split('\\n')
#         # f=f.split(',')
#         print(f)
#         # count=0
#         for i in f[1:len(f)-1]:
#             i=i.split(',')
#             q = Entry.objects.filter(pname=i[0])
#             try:
#                 if not q :
#                     e = Entry()
#                     e.pname = i[0]
#                     e.pqty = i[1]
#                     e.pprice = i[2].replace("\\r","")
#                     e.save()
#                     msg = "Product Saved Properly"
#                     print(msg)        
#                 else:
#                     msg = "Product Already Exists"
#                     print(msg)
#             except:
#                 return HttpResponse('enter proper data')

#     return render(request, 'index.html')




# def index(request):
#     msg=""   
#     if request.POST:
#         f = request.POST['file1']
#         with open(f, 'r') as f:
#             a1 = f.readlines()
#             a = a1[1::]
#             for i in a:
#                 l = i.split(',')                
#                 q = Entry.objects.filter(pname = l[0])
#                 if not q:
#                     e = Entry()
#                     e.pname = l[0]
#                     e.pqty = l[1]
#                     e.pprice = l[2]
#                     e.save()
#                     msg = "Product Saved Properly"
#                     print(msg)        
#                 else:
#                     msg = "Product Already Exists"
#                     print(msg)        

#     return render(request, 'index.html',{msg:'msg'})
   