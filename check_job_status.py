import time

SLEEP_TIME = 5  # seconds to wait

x = start_job()

while True:
    if x.is_finished():
        print("DONE!")
        break
    time.sleep(SLEEP_TIME)
