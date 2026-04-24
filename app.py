import tkinter as tk
import requests
window = tk.Tk()
window.title("useless facts")
window.geometry("1920x1000")
window.resizable(True, True)

prompt = tk.Label(window, text="Would you like to know a useless fact", font=("Arial", 24), wraplength=1920, justify="center")
prompt.pack(pady=10)

def text1():
    prompt.config(text="Did you seriously expect something different?")

def text2():
    prompt.config(text="Are you seriously still here?")

def text3():
    prompt.config(text="Go click the button in the top right then.")

unotext = window.after(3000, text1)
dostext = window.after(5000, text2)
trestext = window.after(10000,text3)
def afact():
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
    if response.status_code != 200:
        print("Error fetching data!") 
        return None
    data = response.json()
    return data

def change_topright_button():
    cancel_task()
    prompt.config(text="you know nothing is going to happen still right..?")

def change_nothing_button():
    prompt.config(text="Bro what is the point of clicking me I do nothing, stop wasting your time")
    unotext
    dostext
    trestext


def change_no_button():
    cancel_task()
    prompt.config(text="Ok smart guy I see how it is, GET OUT!")
    window.after(1500, window.destroy)
def change_button():
    cancel_task()
    afact()
    fact = afact()
    prompt.config(text=(f"{fact['text']} Another one?"))

def cancel_task():
    window.after_cancel(unotext)
    window.after_cancel(dostext)
    window.after_cancel(trestext)

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