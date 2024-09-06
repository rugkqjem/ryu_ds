from minheap import *
class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.frequency = {}
        self.heap = minheap()

    def put(self, lpn):
        #lpn 캐시 안에 있는 경우
        if lpn in self.cache:
            self.update_heap(lpn)
            return 1
        else:
            if len(self.cache) >= self.capacity:
                self.evict_lfu()
            self.cache[lpn] = lpn #캐시에lpn넣어주고
            if lpn in self.frequency:  #lpn빈도확인하고 
                self.frequency[lpn]+=1   #빈도딕셔너리 잇으면 +1 증가해주고
            else:
                self.frequency[lpn]=1     #빈도 딕셔너리에 없으면 새로 만들어주고 +1 
            self.heap.insert([self.frequency[lpn], lpn])  #그러고 힙에 넣어줌
            return -1

    def update_heap(self, lpn):
        # 캐시에 있는 페이지의 빈도가 증가하면 힙을 업데이트
        for i, [freq, page] in enumerate(self.heap._minheap__A):
            if page == lpn:
                # 힙에서 해당 노드 삭제
                del self.heap._minheap__A[i]
                # 빈도 증가
                self.frequency[lpn] += 1
                # 새로운 [빈도, lpn] 노드를 힙에 삽입
                self.heap.insert([self.frequency[lpn], lpn])
                break

    def evict_lfu(self):
        # 캐시 용량을 초과할 경우 LFU 원칙에 따라 가장 적게 사용된 페이지 제거
        evicted_lpn = self.heap.deleteMin()[1]
        del self.cache[evicted_lpn]
        

def lfu_sim(cache_slots):
    cache_hit = 0
    tot_cnt = 0

    cache = LFUCache(cache_slots)

    with open("linkbench.trc") as data_file:
        for line in data_file.readlines():
            lpn = line.split()[0]
            tot_cnt += 1
            if cache.put(lpn) != -1:
                cache_hit += 1

    print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)

if __name__ == "__main__":
    for cache_slots in range(100, 1000, 100):
        lfu_sim(cache_slots)
