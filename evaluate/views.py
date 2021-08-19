from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
     return render(request, 'evaluate/home.html')

           
def EvaluateQuery(request):
    q = request.GET['q']
    try:
        ans = eval(q)
        result = {
            'q':q,
            'ans':ans,
            'error':False,
            'result':True,
        }
        return render(request, 'evaluate/home.html',result)
    
    except:
        result = {
            'error':True,
            'result':False,
        }
        return render(request, 'evaluate/home.html',result)