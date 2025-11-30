import time
import requests

url = "https://community.giffgaff.com"

start = time.time()
r = requests.get(url)
end = time.time()

print(f"Status: {r.status_code}, Time Taken: {end - start:.2f} seconds")
