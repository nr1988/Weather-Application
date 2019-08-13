import tkinter as tk
import requests

HEIGHT=700
WIDTH=800

#def test_function(entry):
 #   print('button clicked ')

#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
#ff9b5e36efa893a90887d4e8ce6ff85a


def format_response(weather):
    try:
        name=weather['name']
        desc=weather['weather'][0]['description']
        temp=weather['main']['temp']


        final_str= 'City:%s \nConditions: %s \nTemperature(°F):%s'%(name,desc,temp)
    except:
        final_str:"There was  a problem retrieving that information"


    return final_str

def get_weather(city):
    weather_key='ff9b5e36efa893a90887d4e8ce6ff85a'
    url= 'https://api.openweathermap.org/data/2.5/weather'
    params={'APPID': weather_key,'q':city, 'units':'imperial'}
    response =requests.get(url,params=params)
    weather=response.json()

    label['text']=format_response(weather)


root = tk.Tk()

canvas= tk.Canvas(root, height=HEIGHT, width=WIDTH )
canvas.pack()

frame = tk.Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1,anchor='n')

entry=tk.Entry(frame, bg='white',font=40)
entry.place( relwidth =0.65, relheight=1)


button = tk.Button(frame, text='Get Weather ' ,font=40, command = lambda:get_weather(entry.get()))
button.place(relx=0.7, relheight=1)


lower_frame=tk.Frame(root,bg='#80c1ff',bd=10)
lower_frame.place(relx=0.5, rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')


label=tk.Label(lower_frame,font=50)
label.place( relwidth=1,   relheight=1)


root.mainloop()


