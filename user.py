import requests
api_key = 'dafe33bbd4f1e143d3888edf18447a44' # Put your API key in this string.
test_url = 'http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=' + api_key

################# IMPORT TEST ################
#resp = requests.get(test_url)
#if resp.status_code in [200, 201]:
#    weather_data = resp.json()
#    print("The weather in {} is {}.".format(weather_data['name'],
#                                            weather_data['weather'][0]['description']))
#else:
#    print("ERROR: " + str(resp.status_code))

############## Current Local Weather ####################
            ######## API BUILD ##################
local_url = 'http://api.openweathermap.org/data/2.5/weather?q=greenville&APPID=' + api_key + '&units=imperial'
getlocal = requests.get(local_url)
localweather = getlocal.json()

        ######### DEBUG #############
#print(localweather)             ##### [dict] - weather, main, name ####
#print(localweather['weather'])  #### [List] - description ####
#print(localweather['main'])     #### [Dict] - Temp, Humidity ####

        ######## BODY #############
print("The weather in {} is {} degrees, with a score of {} Humidity.".format(localweather['name'],
                                    localweather['main']['temp'], localweather['main']['humidity']))

for item in localweather['weather']:
    print("You can expect to see (a) {}".format(item['description']))

################## 5 day forcast #####################
            ######## API BUILD ##################
forcast_url = 'http://api.openweathermap.org/data/2.5/forecast?q=london,uk&APPID=' + api_key + '&units=imperial'
getforcast = requests.get(forcast_url)
londonforcast = getforcast.json()
        ######### DEBUG #############
#print(londonforcast) ### [dict] - list, city  ###
#print(londonforcast)['city'] ### [dict] - name, country ###
#print(londonforcast['list']) ### [list] - main, weather  ###
#for items in londonforcast['list']:
#    print(items['weather']) ### [list][dict] - description ###
#for items in londonforcast['list']:
#    print(items['main']) ### [dict] - temp ###

        ########## BODY #############
#print("The 5-day forcast for weather in {},{} is: ".format(londonforcast['city']['name'], londonforcast['city']['country']))
