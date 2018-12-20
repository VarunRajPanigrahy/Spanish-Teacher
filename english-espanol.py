import requests
import json

key="trnsl.1.1.20181220T181821Z.a672b052bee36df0.0e3e2018f7fde9d7889b3d46e0162ab18744f91f"
selector=int(input("Enter 0 to convert english to spanish. Enter 1 to convert Spanish to english: "))
if(selector==0):
    lang="en-es"
    Format="plain"
    times=int(input("Number of sentences to be translated: "))
    for i in range(times):
        text=(input("Enter text to be translated to spanish: "))

        webpage=("https://translate.yandex.net/api/v1.5/tr.json/translate?key=%s&text=%s&lang=%s")%(key,text,lang)
        response = requests.get(webpage)
        data=response.json()
        print(data["text"][0])
        print(" ")
        if(i==times-1):
            print("Adios!!")
elif(selector==1):
    lang="es-en"
    Format="plain"
    times=int(input("Number of sentences to be translated: "))
    for i in range(times):
        text=(input("Enter Spanish text to be translated to English: "))

        webpage=("https://translate.yandex.net/api/v1.5/tr.json/translate?key=%s&text=%s&lang=%s")%(key,text,lang)
        response = requests.get(webpage)
        data=response.json()
        print(data["text"][0])
        print(" ")
        if(i==times-1):
            print("Adios!!")
    
    
 

