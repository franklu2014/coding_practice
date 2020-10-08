import multiprocessing as mp
import random
import time

magic = 2379

def countMlt(idx, seq, denom):
    tot = 0
    for n in seq:
        if n % denom == 0:
            tot += 1
    return (idx, tot % magic)

if __name__ == '__main__':
    nums = list()
    for _ in range(50):
        nums.append(random.choices(range(int(10000)), k = int(1e6)))
    with mp.Pool(mp.cpu_count()) as pool:
        res1 = list()

        def collect(x):
            global res1
            res1.append(x)

        t1 = time.time()
        for i, lst in enumerate(nums):
            pool.apply_async(countMlt, args = (i, lst, 2), callback = collect)
        pool.close()
        pool.join()
        print(res1)
        print(f"multiprocessing took {time.time() - t1:.3} seconds")
    res2 = list()
    t1 = time.time()
    for i, lst in enumerate(nums):
        res2.append(countMlt(i, lst, 2))
    print(res2)
    print(f"single process took {time.time() - t1:.3} seconds")