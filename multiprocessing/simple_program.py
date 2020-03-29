import time

start = time.perf_counter()


def foo():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done Sleeping...")


foo()
foo()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")

# Output

# Sleeping 1 second...
# Done Sleeping...
# Sleeping 1 second...
# Done Sleeping...
# Finished in 2.0 second(s)
