import requests
import json
from tkinter import*

window=Tk()
window.title("Covid-19")
window.geometry("400x250")

def clicked():
    url="https://api.covid19india.org/data.json"
    page=requests.get(url)
    data=json.loads(page.text)
    lbl.configure(text="Total Active Cases"+data["statewise"][0]["active"])
    lbl1.configure(text="Total Confirmed Cases"+data["statewise"][0]["active"])
    lbl2.configure(text="Data Refreshed")

lbl=Label(window,text="Total Active Cases")
lbl.grid(row=0,column=1)
lbl1=Label(window,text="Total confirmed Cases")
lbl1.grid(row=1,column=1)
lbl2=Label(window,text="")
lbl2.grid(row=3,column=1)
btn=Button(window,text="Refresh",command=clicked)
btn.grid(row=0,column=2)

window.mainloop()