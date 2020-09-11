from django.shortcuts import render
import sys
# from fibonacci import fib

# Create your views here.
def index (request):
    return render(request, 'index.html')

def about (request):
    return  render(request, 'about.html')

def work (request):
    return  render(request, 'work.html')

def contact (request):
    return  render(request, 'contact.html')    

# class recursionlimit:
#     def __init__(self, limit):
#         self.limit = limit
#         self.old_limit = sys.getrecursionlimit()

#     def __enter__(self):
#         sys.setrecursionlimit(self.limit)

#     def __exit__(self, type, value, tb):
#         sys.setrecursionlimit(self.old_limit)

# with recursionlimit(1500):
#     print(fib(1000, 0))        