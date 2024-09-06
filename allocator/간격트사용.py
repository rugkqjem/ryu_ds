import time

class IntervalTreeNode:
    def __init__(self, low, high):
        self.low = low  # 구간의 시작
        self.high = high  # 구간의 끝
        self.max = high  # 현재 노드가 포함된 서브트리의 최대 끝 값
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드

class IntervalTree:
    def __init__(self):
        self.root = None  # 간격 트리의 루트 노드

    def insert(self, root, low, high):
        """새 구간을 간격 트리에 삽입"""
        if not root:
            return IntervalTreeNode(low, high)
        if low < root.low:
            root.left = self.insert(root.left, low, high)
        else:
            root.right = self.insert(root.right, low, high)
        
        if root.max < high:
            root.max = high
        
        return root

    def delete(self, root, low, high):
        """구간을 간격 트리에서 삭제"""
        if not root:
            return root
        if low < root.low:
            root.left = self.delete(root.left, low, high)
        elif low > root.low:
            root.right = self.delete(root.right, low, high)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            temp = self.get_min_value_node(root.right)
            root.low = temp.low
            root.high = temp.high
            root.right = self.delete(root.right, temp.low, temp.high)
        
        root.max = self.get_max(root)
        return root

    def get_min_value_node(self, node):
        """트리에서 최소 값 구간 노드를 찾음"""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def get_max(self, node):
        """노드의 최대 끝 값을 반환"""
        if not node:
            return float('-inf')
        max_val = node.high
        if node.left:
            max_val = max(max_val, node.left.max)
        if node.right:
            max_val = max(max_val, node.right.max)
        return max_val

    def overlap_search(self, root, low, high):
        """주어진 구간과 겹치는 구간을 찾음"""
        if not root:
            return None
        if root.low <= high and low <= root.high:
            return root
        if root.left and root.left.max >= low:
            return self.overlap_search(root.left, low, high)
        return self.overlap_search(root.right, low, high)

    def find_all_overlaps(self, root, low, high):
        """주어진 구간과 겹치는 모든 구간을 찾음"""
        if not root:
            return []
        overlaps = []
        if root.low <= high and low <= root.high:
            overlaps.append(root)
        if root.left and root.left.max >= low:
            overlaps.extend(self.find_all_overlaps(root.left, low, high))
        overlaps.extend(self.find_all_overlaps(root.right, low, high))
        return overlaps

    def insert_interval(self, low, high):
        """새 구간을 간격 트리에 삽입하고 병합"""
        # 병합 가능한 구간을 찾음
        overlapping_intervals = self.find_all_overlaps(self.root, low, high)
        
        # 병합할 구간이 있으면 병합
        if overlapping_intervals:
            for interval in overlapping_intervals:
                low = min(low, interval.low)
                high = max(high, interval.high)
                self.delete_interval(interval.low, interval.high)
        
        # 병합된 구간 삽입
        self.root = self.insert(self.root, low, high)

    def delete_interval(self, low, high):
        """구간을 간격 트리에서 삭제"""
        self.root = self.delete(self.root, low, high)

    def find_best_fit_node(self, root, size):
        """주어진 크기에 가장 적합한 노드를 찾음"""
        if not root:
            return None, None
        if root.high - root.low >= size:
            best_fit_left, best_fit_left_node = self.find_best_fit_node(root.left, size)
            if best_fit_left is None or (root.high - root.low < best_fit_left_node.high - best_fit_left_node.low):
                return (root.low, root.high), root
            return best_fit_left, best_fit_left_node
        return self.find_best_fit_node(root.right, size)

class Allocator:
    def __init__(self):
        self.chunk_size = 4096  # 기본 청크 크기
        self.arena = []  # 할당된 청크를 저장할 리스트
        self.interval_tree = IntervalTree()  # 간격 트리
        self.allocations = {}  # 할당된 메모리를 저장할 딕셔너리
        self.free_counter = 0  # 메모리 해제 횟수 카운터
        self.free_threshold = 10  # 병합을 시도할 메모리 해제 횟수 임계값
        self.start_time = time.time()  # 성능 측정을 위한 시작 시간 기록

    def malloc(self, id, size):
        """주어진 크기의 메모리를 할당하고 id와 연관"""
        best_fit, best_fit_node = self.interval_tree.find_best_fit_node(self.interval_tree.root, size)
        
        if best_fit_node:
            low, high = best_fit
            self.interval_tree.delete_interval(low, high)  # 간격 트리에서도 삭제
            self.allocations[id] = (low, size)
            
            if high - low > size:
                remaining_low = low + size
                remaining_high = high
                self.interval_tree.insert_interval(remaining_low, remaining_high)
        else:
            new_chunk_key = len(self.arena) * self.chunk_size
            self.arena.append(bytearray(self.chunk_size))
            
            # 새로운 청크를 간격 트리에 삽입
            self.interval_tree.insert_interval(new_chunk_key, new_chunk_key + self.chunk_size)
            
            # 새로 할당된 청크에서 메모리 할당을 다시 시도
            return self.malloc(id, size)

    def free(self, id):
        """주어진 id와 연관된 메모리를 해제"""
        if id in self.allocations:
            start, size = self.allocations.pop(id)
            end = start + size
            self.interval_tree.insert_interval(start, end)
            self.free_counter += 1
            if self.free_counter >= self.free_threshold:
                self.free_counter = 0
                self._merge_free_blocks()

    def _merge_free_blocks(self):
        """빈 메모리 블록들을 병합"""
        def merge_intervals(node):
            if not node:
                return None
            left = merge_intervals(node.left)
            right = merge_intervals(node.right)
            if left and left.high == node.low:
                node.low = left.low
                self.interval_tree.delete_interval(left.low, left.high)
            if right and node.high == right.low:
                node.high = right.high
                self.interval_tree.delete_interval(right.low, right.high)
            return node
        
        self.interval_tree.root = merge_intervals(self.interval_tree.root)

    def print_stats(self):
        """현재 메모리 사용 통계를 출력"""
        total_allocated = len(self.arena) * self.chunk_size  # 총 할당된 메모리 크기
        total_used = sum(size for _, size in self.allocations.values())  # 실제 사용 중인 메모리 크기
        utilization = total_used / total_allocated if total_allocated > 0 else 0  # 메모리 활용률
        execution_time = time.time() - self.start_time  # 실행 시간 계산
        print(f"Arena: {total_allocated / (1024 * 1024):.2f} MB")  # 할당된 총 메모리 크기 (MB 단위)
        print(f"In-use: {total_used / (1024 * 1024):.2f} MB")  # 사용 중인 총 메모리 크기 (MB 단위)
        print(f"Utilization: {utilization:.2f}")  # 메모리 활용률
        print(f"Execution Time: {execution_time:.2f} seconds")  # 실행 시간 (초 단위)
        print(f"Total Allocated: {total_allocated} bytes")  # 할당된 총 메모리 크기 (바이트 단위)
        print(f"Total Used: {total_used} bytes")  # 사용 중인 총 메모리 크기 (바이트 단위)

if __name__ == "__main__":
    allocator = Allocator()
    
    with open("allocator/inputdata.txt", "r") as file:
        n = 0
        for line in file:
            req = line.split()
            if req[0] == 'a':
                allocator.malloc(int(req[1]), int(req[2]))  # 메모리 할당 요청 처리
            elif req[0] == 'f':
                allocator.free(int(req[1]))  # 메모리 해제 요청 처리
            
            n += 1
    
    allocator.print_stats()  # 메모리 사용 통계 출력
