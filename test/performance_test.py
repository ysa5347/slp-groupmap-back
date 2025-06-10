import requests
import threading
import time
import os
from dotenv import load_dotenv

def single_test(test_number):
    count = [0]
    t_time = [0.0]
    p_times = []
    lock = threading.Lock()

    def send_request(i):
        try:
            start = time.time()
            response = requests.get(test_url, timeout = 15)
            p_time = time.time() - start # performance time

            with lock:
                p_times.append(p_time)
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

    max_time = max(p_times)
    min_time = min(p_times)
    avg_time = t_time[0] / num_requests
    fail_count = count[0]

    max_times.append(max_time)
    min_times.append(min_time)
    avg_times.append(avg_time)
    fail_counts.append(fail_count)

    print(f"----- Test {test_number} -----")
    print(f"The number of requests : {num_requests}")
    print(f"Failed requests : {fail_count}")
    print(f"Min response time : {round(min_time, 2)} sec")
    print(f"Max response time : {round(max_time, 2)} sec")
    print(f"Average response time : {round(avg_time, 2)} sec")
    print(f"-------------------")

load_dotenv()
test_url = os.getenv("TEST_URL")

num_requests = int(input("Type the number of requests : "))
num_tests = 10
min_times = []
max_times = []
avg_times = []
fail_counts = []

for test_number in range(1, num_tests + 1):
    single_test(test_number)

print("===== Final summary =====")
print(f"Average failed requests : {sum(fail_counts) / num_tests}")
print(f"Minimum response time : {round(min(min_times), 2)} sec")
print(f"Maximum response time : {round(max(max_times), 2)} sec")
print(f"Average response time : {round(sum(avg_times) / num_tests, 2)} sec")
print("=========================")



