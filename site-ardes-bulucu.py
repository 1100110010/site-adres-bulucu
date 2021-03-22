import socket 
from ip2geotools.databases.noncommercial import DpIpCity
url = input("can abi, lütfen linki girermisin? : ")
IP = socket.gethostbyname(url)
response = DpIpCity.get(IP, api_key='free')
print("IP adresi:", IP)
print("bulunduğu şehir:", response.city)
print("bulunduğu bölge:", response.region)
print("bulunduğu ülke:", response.country)
