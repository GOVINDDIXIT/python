import time
import multiprocessing

start = time.perf_counter()


def foo():
    print('Sleeping for 1 second...')
    time.sleep(1)
    print('Done Sleeping...')


p1 = multiprocessing.Process(target=foo)
p2 = multiprocessing.Process(target=foo)

p1.start()
p2.start()

p1.join()
p2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

# Output

# Sleeping for 1 second...
# Sleeping for 1 second...
# Done Sleeping...
# Done Sleeping...
# Finished in 1.07 second(s)
