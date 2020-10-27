from tkinter import*
from tkinter import messagebox
from configparser import ConfigParser
import requests
url='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file='config.ini'
config=ConfigParser()
config.read(config_file)
api_key=config['api_key']['key']


def get_weather(city):
    result=requests.get(url.format(city,api_key))
    if result:
        json=result.json()
        #(city,country,temp_celsius,,temp_fahrenheit,icon,weather)
        city=json['name']
        country=json['sys']['country']
        temp_kelvin=json['main']['temp']
        temp_celsius=temp_kelvin-273.15
        temp_fahrenheit=(temp_kelvin-273.15)*9/5+32
        icon=json['weather'][0]['icon']
        weather=json['weather'][0]['main']
        final=(city,country,temp_celsius,temp_fahrenheit,icon,weather)
        return final
    else:
        return None

def search():
    global image
    city=city_text.get()
    weather=get_weather(city)
    if weather:
        location_lbl['text']='{},{}'.format(weather[0],weather[1])
        temp_lbl['text']='{:.2f}*C,{:.2f}*F'.format(weather[2],weather[3])
        weather_lbl['text']=weather[5]
    else:
        messagebox.showerror('Error','Cannot Find City'.format(city))

root=Tk()
root.title("Weather App")
root.geometry('300x250')
root.configure(background="pink")

city_text=StringVar()
city_entry=Entry(root,textvariable=city_text)
city_entry.pack()
Search_btn=Button(root,text="Search Weather",width=20,command=search)
Search_btn.pack()

location_lbl=Label(root,text='',font=('bold',15))
location_lbl.pack()

image=Label(root,bitmap='')
image.pack()

temp_lbl=Label(root,text='')
temp_lbl.pack()

weather_lbl=Label(root,text='')
weather_lbl.pack()

root.mainloop()