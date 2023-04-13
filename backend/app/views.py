from django.shortcuts import render
from .func import *

def index(request):
    print(request.POST)
    return render(request, "index.html")

def result(request):
    if request.method=='POST':
        age=request.POST["number"]
        gender=request.POST["gender"]
        symptoms=request.POST["symptoms"]
        obj = {
            'age':age,
            'gender':gender,
            'symptoms':symptoms,
        }  

        symptoms_array = list(filter(lambda symptom: symptom != '', obj['symptoms'].split(',\r\n')))
        new_object = {
            'age': obj['age'],
            'gender': obj['gender'],
            'symptoms': symptoms_array
        }
        print(new_object)

        print(predictions(new_object))
        return render(request,"result.html")