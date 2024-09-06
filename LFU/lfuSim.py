from minheap import *

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.frequency = {}
        self.heap = minheap()

    def put(self, lpn):
        if lpn in self.cache:
            self.frequency[lpn] += 1
            self.update_heap(lpn)
            return 1
        else:
            if len(self.cache) >= self.capacity:
                # LFU eviction
                evicted_lpn = self.heap.deleteMin()
                del self.cache[evicted_lpn]
            self.cache[lpn] = lpn
            self.frequency[lpn] = 1
            self.heap.insert((self.frequency[lpn], lpn))
            return -1

    def update_heap(self, lpn):
        for i, (freq, page) in enumerate(self.heap._minheap__A):
          if page == lpn:
            # 빈도 정보 업데이트
            self.heap._minheap__A[i] = (self.frequency[lpn], lpn)
            self.heap.percolateUp(i)  # 힙 재정렬
            break
          
def lfu_sim(cache_slots):
    cache_hit = 0
    tot_cnt = 0

    cache = LFUCache(cache_slots)

    data_file = open("linkbench.trc")

    for line in data_file.readlines():
        lpn = line.split()[0]
        
        data = lpn
        tot_cnt += 1
        if cache.put(lpn) != -1:
            cache_hit += 1

    print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)

if __name__ == "__main__":
    for cache_slots in range(100, 1000, 100):
        lfu_sim(cache_slots)













# def lfu_sim(cache_slots):
#   cache_hit = 0
#   tot_cnt = 0

#   data_file = open("linkbench.trc")


#   for line in data_file.readlines():
#     lpn = line.split()[0]

#     # Program here 

#     #print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)

# if __name__ == "__main__":
#   for cache_slots in range(100, 1000, 100):
#     lfu_sim(cache_slots)
