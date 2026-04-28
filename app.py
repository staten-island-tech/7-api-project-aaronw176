import tkinter as tk
import requests
window = tk.Tk()
window.title("useless facts")
window.geometry("1920x1000")
window.resizable(True, True)
button_press = False

def text1():
    prompt.config(text="Did you seriously expect something different?")

def text2():
    prompt.config(text="Are you seriously still here?")

def text3():
    prompt.config(text="Go click the button in the top right then.")

def text4():
    prompt.config(text="you know nothing is going to happen still right.?")

def text5():
    prompt.config(text="you know nothing is going to happen still right?")

def text6():
    prompt.config(text="...")

def text7():
    prompt.config(text="Alright smart guy you win, go click on the no button")

prompt = tk.Label(window, text="Would you like to know a useless fact", font=("Arial", 24), wraplength=1920, justify="center")
prompt.pack(pady=10)

def afact():
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
    if response.status_code != 200:
        print("Error fetching data!") 
        return None
    data = response.json()
    return data

def change_nothing_button():
    button_pressed()
    try:
        cancel_task_2()
    except NameError:
        ""
    prompt.config(text="Bro what is the point of clicking me I do nothing, stop wasting your time")
    global unotext
    unotext = window.after(3000, text1)
    global dostext
    dostext = window.after(5000, text2)
    global trestext
    trestext = window.after(10000,text3)

def cancel_task():
    try:
        window.after_cancel(unotext)
        window.after_cancel(dostext)
        window.after_cancel(trestext)
    except NameError:
        ""

def change_topright_button():
    cancel_task()
    cancel_task_2()
    global button_press
    if button_press == True:
        prompt.config(text="you know nothing is going to happen still right..?")
        global cuatrotext
        cuatrotext = window.after(15000, text4)
        global cincotext
        cincotext = window.after(20000, text5)
        global seistext
        seistext = window.after(25000, text6)
        global sietetext
        sietetext = window.after(30000, text7)
        button_press = False
    else:
        prompt.config(text="How did you find this button..? buttons unknown?")

def button_pressed():
    global button_press
    button_press = True

def cancel_task_2():
    try:
        window.after_cancel(cuatrotext)
        window.after_cancel(cincotext)
        window.after_cancel(seistext)
        window.after_cancel(sietetext)
    except NameError:
        ""

def change_no_button():
    cancel_task()
    cancel_task_2()
    prompt.config(text="Ok smart guy I see how it is, GET OUT!")
    window.after(1500, window.destroy)

def change_button():
    cancel_task()
    cancel_task_2()
    afact()
    fact = afact()
    prompt.config(text=(f"{fact['text']} Another one?"))

top_right_button = tk.Button(
    window, text="", command=change_topright_button, relief="groove")
top_right_button.place(x=1919,y=0)

fact_button = tk.Button(
    window, text="Yes", font=("Arial", 20), width=20, height=5, command=change_button, relief="groove")
fact_button.place(x=500, y=400)

no_button = tk.Button(
    window, text="No", font=("Arial", 20), width=20, height=5,  command=change_no_button, relief="ridge")
no_button.place(x=1100,y=400)

button = tk.Button(
    window, text="", command=change_nothing_button, relief="groove")
button.place(x=0,y=1000)

window.mainloop()  