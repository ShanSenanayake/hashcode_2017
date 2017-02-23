#!venv/bin/python3

import collections



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

if __name__ == '__main__':
    # 1.put all v.size > cache (in DC) and remove from set
    vs = [v for v in vs if v.size <= cache_size]
    # 2.remove all endpoints without caches
    eps = [ep for ep in eps if ep.caches]
    # 3.remove all requests for endpoints without caches
    rqs = [rq for rq in rqs if rq.ep.caches]
    # 4.(remove all videos no longer requested)
    vs = [v for v in vs if v.requests]
    # 5.{endpoint: {#req/size : video}} video list-map for each endpoint ordered by highest weight
    ep_to_vs = dict()
    for ep in eps:
        vid_list = list()
        for (v, n_req) in ep.videos:
            score = float(n_req)/v.size
            vid_list.append((score, v))
        vid_list = sorted(vid_list, key=lambda x: x[0])
        ep_to_vs[ep] = vid_list

    # 6. Find endpoint which has highest weighted entry.
    # 7. Add video to fastest cache available and remove from all entries which has video cache connected to them
    # 7b if no cache has enough remaining memory, remove video from endpoint-dict
    # 8. Go to 6