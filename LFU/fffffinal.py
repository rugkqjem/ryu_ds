from minheap import *

class LPN_Frequency:
    def __init__(self, lpn, frequency):
        self.lpn = lpn
        self.frequency = frequency

    # 비교 연산자 오버로딩
    def __lt__(self, other):
        return self.frequency < other.frequency

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.frequency = {}  # 새로운 빈도수 딕셔너리 추가
        self.heap = minheap()

    def put(self, lpn):
        # lpn 캐시 안에 있는 경우
        if lpn in self.cache:
            self.update_heap(lpn)
            return 1
        else:
            if len(self.cache) >= self.capacity:
                self.evict_lfu()
            # 캐시에 lpn이 없는 경우
            if lpn in self.frequency:
                frequency = self.frequency[lpn] + 1  # 이미 캐시에 있던 페이지의 빈도수 + 1
            else:
                frequency = 1  # 캐시에 해당 페이지가 처음 추가되는 경우, 빈도수를 1로 초기화
            self.cache[lpn] = lpn
            self.frequency[lpn] = frequency  # 캐시에 페이지 추가 및 빈도수 갱신
            self.heap.insert(LPN_Frequency(lpn, frequency))  # 빈도수와 함께 삽입
            return -1

    def update_heap(self, lpn):
        # 캐시에 있는 페이지의 빈도가 증가하면 힙을 업데이트
        for i, node in enumerate(self.heap._minheap__A):
            if node.lpn == lpn:
                # 힙에서 해당 노드 삭제
                del self.heap._minheap__A[i]
                # 빈도 증가
                node.frequency += 1
                # 새로운 노드를 힙에 삽입
                self.heap.insert(node)
                break

    def evict_lfu(self):
        # 캐시 용량을 초과할 경우 LFU 원칙에 따라 가장 적게 사용된 페이지 제거
        evicted_node = self.heap.deleteMin()
        del self.cache[evicted_node.lpn]

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

    print("cache_slot =", cache_slots, "cache_hit =", cache_hit, "hit ratio =", cache_hit / tot_cnt)

if __name__ == "__main__":
    for cache_slots in range(100, 1000, 100):
        lfu_sim(cache_slots)
