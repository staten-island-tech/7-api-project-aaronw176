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
    print("Why are you here then smart guy")
fact_button = tk.Button(
    window, text="Yes", font=("Arial", 14), command=afact)
fact_button.pack(pady=10)
no_button = tk.Button(
    window, text="No", font=("Arial", 14), command=no_command)
no_button.pack(pady=10)
window.mainloop()