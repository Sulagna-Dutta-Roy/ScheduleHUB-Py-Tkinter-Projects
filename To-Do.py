from tkinter import*
import random

root=Tk()
root.title("My To-Do List")
root.geometry("400x240")


tasks=[]
tasks=["Eat Sushi","Buy a Guiter","Call Mom"]

def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end",task)

def clear_listbox():
    lb_tasks.delete(0,"end")

def add_task():
    task = txt_input.get()
    if task!="":
       tasks.append(task)
       update_listbox()
    else:
        lbl_display["text"]="Please enter a Task"
    txt_input.delete(0,"end")

def delete_all():
    global tasks
    tasks=[]
    update_listbox()

def delete():
    task=lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()

def sort_asc():
    tasks.sort()
    update_listbox()

def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_listbox()

def choose_random():
    task=random.choice(tasks)
    lbl_display["text"]=task

def number_of_tasks():
    number_of_tasks=len(tasks)
    msg="Number of Tasks:%s"%number_of_tasks
    lbl_display["text"]=msg

def exit():
    root.destroy()

lbl_title=Label(root,text="My To-Do List",fg="Black",font=('arial',10,'bold'))
lbl_title.grid(row=0,column=0)
lbl_display=Label(root,text="",fg="Black")
lbl_display.grid(row=0,column=1)

txt_input=Entry(root,width=15)
txt_input.grid(row=1,column=1)

btn_add_task=Button(root,text="Add Task",fg="Black",command=add_task)
btn_add_task.grid(row=1,column=0)
btn_delete_all=Button(root,text="Delete All",fg="Black",command=delete_all)
btn_delete_all.grid(row=2,column=0)
btn_delete=Button(root,text="Delete",fg="Black",command=delete)
btn_delete.grid(row=3,column=0)
btn_sort=Button(root,text="Sort(ASC)",fg="Black",command=sort_asc)
btn_sort.grid(row=4,column=0)
btn_sort=Button(root,text="Sort(DESC)",fg="Black",command=sort_desc)
btn_sort.grid(row=5,column=0)
btn_choose_random=Button(root,text="Choose Random",fg="Black",command=choose_random)
btn_choose_random.grid(row=6,column=0)
btn_number_of_tasks=Button(root,text="Number Of Tasks",fg="Black",command=number_of_tasks)
btn_number_of_tasks.grid(row=7,column=0)
btn_exit=Button(root,text="Exit",fg="Black",command=exit)
btn_exit.grid(row=8,column=0)

lb_tasks=Listbox(root)
lb_tasks.grid(row=1,column=1,rowspan=9)

root.mainloop()