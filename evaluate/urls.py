from django.urls import path
from .views import home,EvaluateQuery

urlpatterns = [ 
    path('', home, name='home'),
    path('evaluate-query',EvaluateQuery, name="evaluate-query")
]

