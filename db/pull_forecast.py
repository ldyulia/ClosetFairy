import requests, json
import pyrebase
import time

config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "storageBucket": ""
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

api_key = ""
owm_url = "http://api.openweathermap.org/data/2.5/forecast?"


# country = ""
cities = [1832257, 1832501, 1832743, 1832909, 1840886, 1841976, 
1845519, 1846095, 1925943, 1845106, 6802827, 1890085, 1833702, 
6367618, 6573030, 1842936, 6800892, 6800397, 1844533, 1832215, 1832697, 
1832830, 1832847, 1833466, 1833514, 1833788, 1835096, 1838722, 
1839726, 1840862, 1841810, 1841988, 1842016, 1842153, 1842225, 1842754,
1842944, 1843082, 1843847, 1844045, 1844174, 1844191, 1846114, 1846355, 
1886598, 1892823, 1896953, 1897000, 1897118, 1925936, 6903078, 1833581, 
1884249, 1835518, 1846278, 1844539, 1832015, 1832617, 1835447, 1835967, 
1836208, 1838508, 1839011, 1840179, 1842966, 1843585, 1844308, 1847050, 
1882056, 1912205, 6395804, 1835841, 1902028, 1846430, 6901961, 6901967, 
1841597, 6890843, 1845105, 1846589, 6887688, 6891973, 1837660, 1844088, 
1886748, 6895286, 6812754, 6812988, 6794644, 1841610, 1844106, 6575822, 
6575866, 1843880, 6575891, 6398879, 1843125, 6808346, 1845275, 6795956, 
6576320, 6573457, 6795865, 6803229, 6800516, 6367745, 1883978, 
1846986, 6800746, 1846735, 1837055, 1833747, 1838524,
1846918, 1835329, 1842943, 1840898, 1833105, 1841245, 1845789, 
1843491, 1832427, 1838343, 1846052, 1838716, 1841811, 1846265,
1846266, 1842030, 1832828, 1845604, 1845136, 1842485, 1839071, 1897122, 
1845759, 1845788, 1841775, 1832771, 1842616, 1846069, 1842025, 1841066, 
1846898, 1845457, 1832157, 1836553, 1897007, 1841909, 1843137, 1835648, 
1841149, 1835650, 1894079, 1846149, 1845033, 1844788, 1837706, 1835895, 
1839652, 6571507, 1837217, 1838740, 1832663, 1843702, 1842939, 1840211, 
1832566, 1840421, 1843542, 1832809, 1842518, 1832384, 1841598, 1840942, 
1840379, 1844751, 1840982, 1843841, 1840536, 1841603, 1842781, 1840454, 
1948005, 1842859, 1835515, 1949757, 6367665, 1842800, 1841919, 1844954, 
6799737, 1844192, 6801953, 1838294, 1838431, 1842559, 1833763, 1840377, 
1930831, 6897324, 1834885, 1843163, 1839873, 1838069, 1832798, 
1895287, 1843495, 1843502, 1845585, 6575883, 6575423, 1836164, 1836034, 
1979031, 1832008, 7588461, 6794156, 6816630, 7588425, 1837640, 6877998, 
1885994, 1886130, 1832973, 1835235, 1835553, 1835848, 1843564, 1846326, 
1846912, 1912209, 6573747, 6800035, 6811761]

# celsius = metric, fahrenheit = imperial, dafault = kelvin
unit = "metric"

res = {}
for cityid in cities:
    weather_url = owm_url + "appid=" + api_key + "&id=" + str(cityid) + "&units=" + unit
    weather_req = requests.get(weather_url)
    curr_weather = weather_req.json()

    if curr_weather["cod"] != "404":
        day = curr_weather["list"][0:8]
        cityname = curr_weather["city"]["name"]
        med_list = []
        for info in day:
            data = {}
            data["dt_utc"] = info["dt"]
            data["dt_txt"] = info["dt_txt"]
            data["weather"] = info["weather"][0]["main"]
            data["temp"] = info["main"]["temp"]
            data["cityname"] = cityname
            if info["main"].get("feels_like"): 
                data["feels_like"] = info["main"]["feels_like"]
            med_list.append(data)
        if cityid not in res.keys():
            res[cityid] = med_list
    else:
        print("city ID not exist", cityid)
    time.sleep(1)


db.child("OWM").update(res)





        		

        	






