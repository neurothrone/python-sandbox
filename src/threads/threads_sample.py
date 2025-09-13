import threading
import time


def sleep(seconds: int, results: dict = None):
    time.sleep(seconds)
    print(f"Finished sleeping for {seconds} seconds.")
    if results is not None:
        results[seconds] = "Done"


if __name__ == "__main__":
    thread_results = {}

    threads = [threading.Thread(target=sleep, args=(n, thread_results)) for n in range(5)]
    [t.start() for t in threads]
    [t.join() for t in threads]

    print("All threads finished.")
    print(thread_results)
