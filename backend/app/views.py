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
        # print(new_object)
        a=predictions(new_object)
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

                    if a in row:


                        desired_value2="1."+row[1]+"\n"+"2."+row[2]+"\n"+"3."+row[3]+"\n"+"4."+row[4]
            prevention=desired_value2

        return render(request,"result.html",{'description':description,'a':a,'prevention':prevention})