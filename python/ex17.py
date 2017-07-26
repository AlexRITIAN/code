import time

while True:
    try:
        input()
        start = time.time()
        print("started")
    except KeyboardInterrupt:
        end = time.time()
        print("end")
        print("Total : ",round(end - start, 2),"secs")
        break
