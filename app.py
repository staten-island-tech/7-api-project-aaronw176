import requests
def afact(anime_name):
    response = requests.get("https://anime-facts-rest-api.herokuapp.com/api/v1")
    if response.status_code != 200:
        print("Error fetching data!") 
        return None
    data = response.json
afact("bleach")