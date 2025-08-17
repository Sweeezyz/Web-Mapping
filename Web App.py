import folium
import pandas


#Basic Assignment
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

#Function to categorize the elevations
def colr_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<=elevation < 3000:
        return 'orange'
    else:
        return 'red'

#25.19455896771803, 55.27342202760992

#Starting point coordinates, zoom strength and tiles
map = folium.Map(location=[35.58, -99.09], zoom_control=18, tiles="Cartodb Positron")

#Simple group to make life easier
featureGroupVolcanoes = folium.FeatureGroup(name="Volcanoes")
featureGroupTouristic = folium.FeatureGroup(name="Touristic")
featureGroupKnown = folium.FeatureGroup(name="Known Locations")
featureGroupPopulations = folium.FeatureGroup(name="Population")
featureGroup = folium.FeatureGroup(name="All")


touristic = [[25.19748651734144, 55.27970174377592], [25.19455896771803, 55.27342202760992], [25.118320691214723, 55.201165895345916], [25.134797632468107, 55.11674646871765]]
known = [[25.311773551579392, 55.4926932112463], [25.21214411454512, 55.41811700285921]]


#Using .txt file
for lt, ln, nm, el in zip(lat, lon, name, elev): #Volcanoes
    featureGroupVolcanoes.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=nm+ " "+str(el)+"m", fill_color=colr_producer(el), color='grey', fill_opacity=0.7))
    featureGroup.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=nm+ " "+str(el)+"m", fill_color=colr_producer(el), color='grey', fill_opacity=0.7))


#Personal locations
for coordinates in touristic: #Dubai
    featureGroupTouristic.add_child(folium.CircleMarker(location=coordinates, radius=6, popup="Touristic Sites", color='white', fill_color='blue', fill_opacity=0.7))
    featureGroup.add_child(folium.CircleMarker(location=coordinates, radius=6, popup="Touristic Sites", color='white', fill_color='blue', fill_opacity=0.7))

for coordinates in known: #Dubai+Sharjah
    featureGroupKnown.add_child(folium.CircleMarker(location=coordinates, radius=6, popup="Known Locations", color='white', fill_color='pink', fill_opacity=0.7))
    featureGroup.add_child(folium.CircleMarker(location=coordinates, radius=6, popup="Known Locations", color='white', fill_color='pink', fill_opacity=0.7))


#Using .json file to categorize the populations across the world
featureGroupPopulations.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] <20000000 else 'red' }))

#Creating the layers
map.add_child(featureGroupVolcanoes)
map.add_child(featureGroupPopulations)
map.add_child(featureGroupTouristic)
map.add_child(featureGroupKnown)
map.add_child(featureGroup)
map.add_child(folium.LayerControl())

map.save("Map1_Dubai.html")