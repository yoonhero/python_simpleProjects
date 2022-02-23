import requests
import time
target_IP = "http://172.30.1.8/"

i = 1

while True:
    response = requests.get(target_IP)
    time.sleep(0.00001)
    print("pakcet sent ", i)
    i += 1
