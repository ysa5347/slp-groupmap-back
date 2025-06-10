import requests
import threading
import time
import os
from dotenv import load_dotenv

load_dotenv()
test_url = os.getenv("TEST_URL")

num_requests = int(input("Type the number of requests : "))
count = [0]
t_time = [0.0]
lock = threading.Lock()

def send_request(i):
    try:
        start = time.time()
        response = requests.get(test_url)
        p_time = time.time() - start # performance time

        with lock:
            t_time[0] += p_time
            if response.status_code != 200:
                count[0] += 1

        print(f"{i}: {response.status_code}")
    except Exception as e:
        print(f"{i}: Error - {e}")
        count[0] += 1

threads = []

for i in range(num_requests):
    t = threading.Thread(target=send_request, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("The number of requests : " + str(num_requests))
print("Average performance time : " + str(t_time[0] / num_requests))
print("The number of failed requests : " + str(count[0]))
