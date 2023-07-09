import requests

url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

jagah = input("Enter the name of city")

querystring = {"city":{jagah}}

headers = {
	"X-RapidAPI-Key": "b0cec84022msh05f3e5207ccc03dp1aab46jsn77e618091477",
	"X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())