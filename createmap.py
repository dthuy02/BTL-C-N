import folium
import requests
import webbrowser

def get_route(start_coords, end_coords):
    url = f"https://router.project-osrm.org/route/v1/driving/{start_coords[1]},{start_coords[0]};{end_coords[1]},{end_coords[0]}?steps=true&geometries=geojson"
    response = requests.get(url)
    data = response.json()
    route_geometry = data['routes'][0]['geometry']
    return route_geometry

def generate_route_map(start_coords, end_coords):
    mymap = folium.Map()
    route_geometry = get_route(start_coords, end_coords)
    route_line = folium.PolyLine(locations=[list(reversed(coord)) for coord in route_geometry['coordinates']], color='blue')
    route_line.add_to(mymap)
    folium.Marker(list(reversed(start_coords)), popup='Start', icon=folium.Icon(color='green')).add_to(mymap)
    folium.Marker(list(reversed(end_coords)), popup='End', icon=folium.Icon(color='red')).add_to(mymap)
    mymap.fit_bounds([[coord[1], coord[0]] for coord in route_geometry['coordinates']])
    file_path = 'route_map.html'
    mymap.save(file_path)
    webbrowser.open(file_path)  # Mở tệp HTML trong trình duyệt mặc định của hệ thống

# Example usage
start_coords = (20.9944171, 105.8171316)  
end_coords = (21.0365377, 105.8285908)  

generate_route_map(start_coords, end_coords)
