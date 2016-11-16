import multiprocessing


def spawn(num):
    print("Spawn! {}".format(num))

if __name__ == "__main__":
    for i in range(100):
        p = multiprocessing.Process(target=spawn, args=(i, i + 1))
        p.start()
        # p.join()
