from django.shortcuts import render
from .func import *
import csv 

def index(request):
    # print(request.POST)
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
        
        a=predictions(new_object)[0]
        with open('static/symptom_Description.csv', mode='r') as csv_file:

            csv_reader = csv.reader(csv_file)

            for row in csv_reader:

                if a in row:

                    desired_value = row[1]  
            print(predictions(new_object))
            print(desired_value)

        description=desired_value  
        
        with open('static/symptom_precaution.csv',mode='r') as csv_file:

            csv_reader=csv.reader(csv_file)

            for row in csv_reader:
                    if a in row[0]:
                        dv=[row[1],row[2],row[3],row[4]]
        return render(request,"result.html",{'a':a,'description':description,'d1':dv[0],'d2':dv[1],'d3':dv[2],'d4':dv[3]})