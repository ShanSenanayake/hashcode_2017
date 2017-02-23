import sys

class Ep:

    def __init__(self, index, latency):
        self.index = index
        self.latency = latency
        self.caches = list()

    def add_cache(self, cache, latency):
        self.caches.append((cache, latency))
        cache.eps.append((self, latency))

class Cache:

    def __init__(self, index):
        self.index = index
        self.eps = list()



def main(args):
    with open(args[0], 'r') as f:
        print(f.readline())

if __name__ == "__main__":
    main(sys.argv[1:])
