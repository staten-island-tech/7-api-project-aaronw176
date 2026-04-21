import tkinter as tk
import requests
window = tk.Tk()
window.title("useless facts")
window.geometry("400x250")
window.resizable(False, False)
prompt = tk.Label(window, text="Would you like to know a useless fact", font=("Arial", 16))
prompt.pack(pady=10)
def afact():
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
    if response.status_code != 200:
        print("Error fetching data!") 
        return None
    data = response.json()
    print(data['text']) 
def no_command():
    print("Ok smart guy I see how it is")
def nothing():
    print("Bro what is the point of clicking me I do nothing, stop wasting your time")
fact_button = tk.Button(
    window, text="Yes", font=("Arial", 14), width=10, command=afact)
fact_button.place(x=60, y=75)
no_button = tk.Button(
    window, text="No", font=("Arial", 14), width=10, command=no_command)
no_button.place(x=225,y=75)
button = tk.Button(
    window, text="", font=("Arial", 14), command=nothing)
button.place(x=195,y=60)
window.mainloop()  