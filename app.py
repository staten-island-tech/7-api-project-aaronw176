import tkinter as tk
import requests
window = tk.Tk()
window.title("useless facts")
window.geometry("400x250")
window.resizable(False, False)

def afact(amount):
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
    if response.status_code != 200:
        print("Error fetching data!") 
        return None
    data = response.json()
    print(data['text'])
afact(1)
