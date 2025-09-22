import threading
import random
import time

N = 1000000

def monteCarlomethod(points, results, indx):
    in_circle = 0
    for _ in range(points):
        x =  random.random()
        y = random.random()
        if x*x + y*y <= 1.0:
            in_circle += 1
    results[indx] = in_circle


def runforthreads(n_thr):
    p_thread = N // n_thr
    results = [0] * n_thr
    threads = []

    start = time.time()

    for i in range(n_thr):
        t = threading.Thread(target=monteCarlomethod, args=(p_thread, results, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total_in = sum(results)
    pi_est = 4 * total_in / (p_thread * n_thr)
    end = time.time()

    return pi_est, end - start


if __name__ == "__main__":
    print("Main thread: ")
    start = time.time()
    inside = 0
    for _ in range(N):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1.0:
            inside += 1
    pi_est = 4 * inside / N
    end = time.time()
    print(f"PI ≈ {pi_est:.6f}, час = {end - start:.4f} сек")

    print("\nParallel threads: ")
    for threads in [2, 4, 8, 16, 32, 64]:
        pi_est, elapsed = runforthreads(threads)
        print(f"Threads={threads:2d}: PI ≈ {pi_est:.6f}, час = {elapsed:.4f} сек")
