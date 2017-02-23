import sys

class Ep:

    def __init__(self, index, latency):
        self.index = index
        self.latency = latency
        self.videos = list()
        self.caches = list()

    def add_cache(self, cache, latency):
        self.caches.append((cache, latency))
        cache.eps.append((self, latency))

    def add_video(self, video, request):
        self.videos.append((video, request))
        video.eps.append((self, request))

class Cache:

    def __init__(self, index, size):
        self.index = index
        self.size = size
        self.eps = list()

class Video:

    def __init__(self, index, size):
        self.index = index
        self.size = size
        self.eps = list()


def main(args):
    with open(args[0], 'r') as f:
        v, e, r, c, x = [int(i) for i in f.readline().split(' ')]
        video_dict = dict()
        for i, s in enumerate(f.readline().split(' ')):
            video_dict[i] = Video(i,int(s))
        l = list()
        cache_dict = dict()
        ep_dict = dict()


        for index in range(e):
            lt, k = [int(i) for i in f.readline().split(' ')]
            ep = Ep(index, lt)
            ep_dict[index] = ep
            for _ in range(k):
                temp = f.readline().split(' ')
                cache_i, lat = [int(i) for i in temp]
                if cache_i not in cache_dict:
                    cache_dict[cache_i] = Cache(cache_i, x)
                ep.add_cache(cache_dict[cache_i], lat)

        for _ in range(r):
            rv, re, rn = [int(i) for i in f.readline().split(' ')]
            ep_dict[re].add_video(video_dict[rv], rn)



if __name__ == "__main__":
    main(sys.argv[1:])
