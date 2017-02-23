import sys

class Ep:

    def __init__(self, index, latency, ep_map):
        self.index = index
        self.latency = latency
        self.videos = dict()
        self.caches = dict()
        self.ep_map = ep_map


    def add_cache(self, cache, latency):
        self.caches[cache.index] = (cache, latency)
        cache.eps[self.index] = (self, latency)

    def add_video(self, video, request):
        self.videos[video.index] = (video, request)
        video.eps[self.index] = (self, request)

    def remove(self):
        for v in self.videos.values():
            del v.eps[self.index]
        for c in self.caches.values():
            del c.eps[self.index]
        del ep_map[self.index]


class Cache:

    def __init__(self, index, size):
        self.index = index
        self.size = size
        self.videos = dict()
        self.eps = dict()

    def add_video(self, video):
        self.videos[video.index] = video
        video.caches[self.index] = self
        self.size -= video.size

    def remove_video(self, video):
        del self.videos[video.index]
        del video.caches[self.video]
        self.size += video.size

class Video:

    def __init__(self, index, size, video_map):
        self.index = index
        self.size = size
        self.eps = dict()
        self.video_map = video_map

    def remove(self):
        for ep in eps.values():
            del ep.videos[self.index]
        del video_map[self.index]


def parse(args):

    video_dict = dict()
    cache_dict = dict()
    ep_dict = dict()
    with open(args[0], 'r') as f:
        v, e, r, c, x = [int(i) for i in f.readline().split(' ')]
        for i, s in enumerate(f.readline().split(' ')):
            s = int(s)
            if s <= x:
                video_dict[i] = Video(i,int(s), video_dict)

        l = list()
        cache_dict = dict()
        ep_dict = dict()


        for index in range(e):
            lt, k = [int(i) for i in f.readline().split(' ')]
            ep = Ep(index, lt, ep_dict)
            if k != 0:
                ep_dict[index] = ep
            for _ in range(k):
                temp = f.readline().split(' ')
                cache_i, lat = [int(i) for i in temp]
                if cache_i not in cache_dict:
                    cache_dict[cache_i] = Cache(cache_i, x)
                ep.add_cache(cache_dict[cache_i], lat)

        for _ in range(r):
            rv, re, rn = [int(i) for i in f.readline().split(' ')]
            if re in ep_dict:
                ep_dict[re].add_video(video_dict[rv], rn)

    return (video_dict, cache_dict, ep_dict)


if __name__ == "__main__":
    parse(sys.argv[1:])
