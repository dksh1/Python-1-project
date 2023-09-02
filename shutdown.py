from tkinter import *
import os

def restart():
    os.system("ShutDown /r /t 1")
def restart_time():
    os.system("ShutDown /r /t 20")
def logout():
    os.system("ShutDown -l")
def shutdown():
    os.system("ShutDown /s /t 1")



st = Tk()

st.title("ShutDown App")
st.geometry("700x500")
st.config(bg="Dark Blue")

r_button = Button(st,text="Restart",font=("Arial",20,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=250,y=60,height=50,width=150)

rt_button = Button(st,text="Restart time",font=("Arial",20,"bold"),relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=250,y=170,height=50,width=150)

rl_button = Button(st,text="Log-out",font=("Arial",20,"bold"),relief=RAISED,cursor="plus",command=logout)
rl_button.place(x=250,y=270,height=50,width=150)

rl_button = Button(st,text="ShutDown",font=("Arial",20,"bold"),relief=RAISED,cursor="plus",command=shutdown)
rl_button.place(x=250,y=370,height=50,width=150)




st.mainloop()
