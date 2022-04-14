import requests
import datetime



APP_ID="your key"
APP_KEY="your key"

GENDER="male"
WEIGHT=80
HEIGHT=187
AGE=19
Exercise_text=input("enter what you did")
parameters={
    "query":Exercise_text,
    "gender":"male",
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE,


}
headers={
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY,



}
header_for_sheety={
    "Authorization": "Bearer hellomoto"
}



request=requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",headers=headers,json=parameters)
request.raise_for_status()

data=request.json()
# activity=
print(data)
today_date=datetime.datetime.now().date()
today_time=datetime.datetime.now().strftime("%H:%M:%S")
print(today_time)


for i in data['exercises']:
    sheet_dis = {
        "sheet1": {
            "date": f"{today_date}",
            "time": today_time,
            "exercise": i['name'],
            "duration": i['duration_min'],
            "calories": i['nf_calories'],
        }
    }


    request_sheety = requests.post(url="https://api.sheety.co/c19443fc303282080c6d70d99ff9d706/newOne/sheet1",json=sheet_dis,headers=header_for_sheety)
    print(request_sheety.text)




