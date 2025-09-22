import threading
import time

def calcSum(threadId, start, end):
    sum = 0
    for i in range(start, end+1):
        sum+=i
        time.sleep(0.001)
    print(f"Thread {threadId}: Sum: {sum}")

if __name__ == "__main__":
    r1 = (0, 100)
    r2 = (100, 200)

    t1 = threading.Thread(target=calcSum, args=(1, r1[0], r1[1]))
    t2 = threading.Thread(target=calcSum, args=(2, r2[0], r2[1]))
    print("Start thread")
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Finish")