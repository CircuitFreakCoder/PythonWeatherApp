"""

Copyright (c) 2013 Jorick A. Caberio and contributors

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 

documentation files (the "Software"), to deal in the Software without restriction, including without limitation

the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and 

to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of 

the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO 

THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS 

OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 

OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""


import json,  urllib2, Tkinter, tkSimpleDialog, tkMessageBox

def fetchHTML(url):
    URL = "http://openweathermap.org/data/2.1/find/name?q="+url
    req = urllib2.Request(URL)
    response=urllib2.urlopen(req)
    return response.read()

root = Tkinter.Tk()
root.withdraw()

tkMessageBox.showinfo("About","Python Weather App \nUsing Open Weather Maps API")

input_location = tkSimpleDialog.askstring("Weather App", "Enter a Location\n")
output=fetchHTML(input_location)
data = json.loads(output)

tkMessageBox.showinfo("Results", "Location: " + str(data['list'][0]['name']) +
"\n\nCountry: " + str(data['list'][0]['sys']['country']) + "\n\nLatitude: " + str(data['list'][0]['coord']['lat'])+
"\n\nLongitude: " +str(data['list'][0]['coord']['lon']) + "\n\nTemperature: "+str(data['list'][0]['main']['temp']-273.15) +" C"+
"\n\nHumidity: " + str(data['list'][0]['main']['humidity']) + " %"+
"\n\nPressure: " + str(data['list'][0]['main']['pressure']) + " hPa"+
"\n\nWind Speed: " + str(data['list'][0]['wind']['speed']) + " mps" +
"\n\nWeather Description: " + str(data['list'][0]['weather'][0]['description']) )                                                     

