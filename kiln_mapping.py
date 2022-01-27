import pandas as pd
import folium
from folium.plugins import FloatImage
import streamlit as st
from streamlit_folium import folium_static

brick_kiln_data = pd.read_csv("baseline_quex_v3 (2) (1).csv")

def marker_color(row):
    if row['begin_general_information-kiln_id'] in [2,5,8,10,11,17,18,19,20,22,23]:
        return 'cadetblue'
    elif row['begin_general_information-kiln_id'] in [4,6,7,9,13,14,21,24,27,28,29]:
        return 'blue'
    else:
        return 'pink' 
    
brick_kiln_data['color'] = brick_kiln_data.apply(marker_color, axis=1)

st.set_page_config(layout='wide')

st.write("### Clean Brick Manufacturing Project: icddr,b")
st.write("### Brick Kiln Locations in Jessore")

image_file = 'legends.png'
st.image(image_file, width=800)

fol_map = folium.Map(
    location=[23.170664,89.212418],
    zoom_start=11
)

for i in range(brick_kiln_data.shape[0]):
    kiln = brick_kiln_data.loc[i]
    folium.Marker(
        location=[kiln['begin_general_information-geopoint-Latitude'], kiln['begin_general_information-geopoint-Longitude']],
        tooltip=kiln['begin_general_information-kiln_name'],
        popup= kiln['begin_general_information-address'],
        icon=folium.Icon(color=kiln['color'])
    ).add_to(fol_map)


# title_html = '''
#              <h3 align="center" style="font-size:20px"><b>Brick KIln Locations: Clean Brick Manufacturing Project</b></h3>
#              '''
# fol_map.get_root().html.add_child(folium.Element(title_html))

folium_static(fol_map, width=1250, height=700)

