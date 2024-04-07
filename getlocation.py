import requests
import subprocess
import folium
import webbrowser


def geocode_address(address):
    url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json"
    response = requests.get(url)
    data = response.json()
    if data:
        latitude = float(data[0]['lat'])
        longitude = float(data[0]['lon'])
        return latitude, longitude
    else:
        print("Không tìm thấy địa điểm.")
        return None, None

def generate_route(address1, address2):
    latitude1, longitude1 = geocode_address(address1)
    latitude2, longitude2 = geocode_address(address2)
    if latitude1 is not None and longitude1 is not None and latitude2 is not None and longitude2 is not None:
        generate_route_map((latitude1, longitude1), (latitude2, longitude2))  # Sửa đổi tên hàm
        print(f"Tọa độ của {address1}: {latitude1}, {longitude1}")
        print(f"Tọa độ của {address2}: {latitude2}, {longitude2}")
    else:
        print("Không thể tạo bản đồ do không tìm thấy địa điểm.")

# Example usage
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
