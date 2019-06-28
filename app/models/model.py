import requests
def get_runtime_by_title(title): 
    print(title)
    response = requests.get('http://www.omdbapi.com/?apikey=e4402686&t=' + str(title)).json()
    print(response)
    return response["Runtime"]





def get_popcorn_size(minutes):
    hours = minutes / 60
    if hours < 1:
        size = "Small Popcorn"
    elif hours >= 1 and hours < 2:
        size = "Medium Popcorn"
    elif hours >= 2 and hours < 3:
        size = "Large Popcorn"
    elif hours >= 3 and hours <= 4:
        size = "X-tra Large Popcorn"
    elif hours > 4:
        size = "whole meal for this" 
    return size

def getanswers(info):
    response = requests.get('http://www.omdbapi.com/?apikey=e4402686&t=' + str(info)).json()
    return [response["Runtime"], response["Title"], response["Year"], response["imdbRating"]]

    

