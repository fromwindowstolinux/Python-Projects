import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(el):
    if el < 1000:
        return "green"
    elif 1000 <= el < 2000:
        return "orange"
    else:
        return "red"

html = """
Volcano name: <br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>
<br>
Height: %s m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")

# Volcanoes

feature_group_volcanoes = folium.FeatureGroup(name="Volcanoes")

for latitude, longitude, elevation, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, elevation), width=200, height=100)
    feature_group_volcanoes.add_child(folium.CircleMarker(location=[latitude, longitude], radius=6, popup=folium.Popup(iframe), fill_color=color_producer(elevation), color="grey", fill_opacity=0.7, fill=True))

# Population 

feature_group_population = folium.FeatureGroup(name="Population")

feature_group_population.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), 
style_function=lambda x: 
{"fillColor":"green" if x["properties"]["POP2005"] < 10000000 
else "orange" if 1000000 <= x["properties"]["POP2005"] < 20000000
else "red"}))

map.add_child(feature_group_volcanoes)
map.add_child(feature_group_population)

# Top Right Box
map.add_child(folium.LayerControl())

map.save("map1.html")