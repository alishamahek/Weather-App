import requests
import json
import win32com.client
while True:

    city = input("Enter A city: ")
    url = f"https://api.weatherapi.com/v1/current.json?key=2958397c00b842db92e125039241605&q={city}"
    info = requests.get(url)
    # print(info.text)
    wdic = json.loads(info.text)
    # print(wdic["current"] ["temp_c"])
    speaker = win32com.client.Dispatch("Sapi.SpVoice")
    speaker.Speak(wdic["current"] ["temp_c"])
    # speaker.Speak(wdic["current"] ["condition])
    if city == "q":
        break
