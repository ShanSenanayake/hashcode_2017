#!venv/bin/python3

import collections
import sys
import parser

# {k: ep_to_vs[k] for k in sorted(d, key=lambda k: d[k][0])}
# vid_list = sorted(ep_to_vs, key=lambda x: x[1])

# 1.put all v.size > cache (in DC) and remove from set
# 2.remove all endpoints without caches
# 3.remove all requests for endpoints without caches
# 4.(remove all videos no longer requested)
# 5.{endpoint: {#req/size : video}} video list-map for each endpoint ordered by highest weight
# 6. Find endpoint which has highest weighted entry.
# 7. Add video to fastest cache available and remove from all entries which has video cache connected to them
# 7b if no cache has enough remaining memory, remove video from endpoint-dict
# 8. Go to 6

# 5.{endpoint: [{Video:#requests}] (map with endpoint to V:s and requests)
# 4.

# WHEN REMOVING videos or requests, make sure to remove alll references to them

def get_best_end_point(ep_to_vs, ep_dict):
    # @TODO: implement using max, not sort
    sorted_list = sorted(ep_to_vs, key=lambda k: ep_to_vs[k][0])
    return ep_dic[sorted_list[0]] if soreted_list else None

def get_best_cache(ep, video):
    best_cache = None
    for cache in ep.caches.values():
        if cache.size >= video.size:
            # @TODO: + if cache has many neighbours with this movie highly ranked
            if best_cache and best_cache.latency > cache.latency:
                best_cache = cache
            elif not best_cache:
                best_cache = cache
    return best_cache


if __name__ == '__main__':

    (video_dict, cache_dict, ep_dict) = parser.parse(sys.args[:1])
    # 4.(remove all videos no longer requested)
    video_dict = {k: v for k, v in video_dict.items() if not [ep for ep in ep_dict.values() if ep.videos.contains(v.id)]}
    # 5.{endpoint: {#req/size : video}} video list-map for each endpoint ordered by highest weight
    ep_to_vs = dict()
    for ep in ep_dict.values():
        vid_list = list()
        for v, n_req in ep.videos.values():
            score = float(n_req)/v.size
            vid_list.append((score, v))
        vid_list = sorted(vid_list, key=lambda x: x[0])
        ep_to_vs[ep.index] = vid_list
    # ep_to_vs[k] for k in sorted(d, key=lambda k: d[k][0])

    # BEGIN LOOP
    # 6. Find endpoint which has highest weighted entry.
    while best_ep = get_best_end_point(ep_to_vs):

        best_video = ep_to_vs[best_ep.index].pop()[1]

        # 6.5 find best cache
        best_cache = get_best_cache(best_ep, best_video)
        # 7b if no cache has enough remaining memory, remove video from endpoint-dict
        if not best_cache:
            ep.remove_video(best_video)
            # remove video from ep and continue
        else:
            # 7b. Add video to fastest cache available and remove from all entries which has video cache connected to them
            cache.add_video(video, ep_to_vs)
        # 8. Go to 6

    for cache in cache_dict.values():
        print(cache.index, *cache.keys())

