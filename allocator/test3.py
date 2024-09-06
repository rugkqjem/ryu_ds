import time

class AVLTreeNode:
    def __init__(self, key, size):
        self.key = key  # 노드의 시작 주소
        self.size = size  # 메모리 블록의 크기
        self.height = 1  # AVL 트리의 높이
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드

class AVLTree:
    def __init__(self):
        self.root = None  # AVL 트리의 루트 노드

    def get_height(self, node):
        """노드의 높이를 반환"""
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        """노드의 균형 인수를 반환"""
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        """오른쪽 회전 수행"""
        x = y.left
        T2 = x.right if x else None
        if x:
            x.right = y
        y.left = T2
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        if x:
            x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        return x

    def left_rotate(self, x):
        """왼쪽 회전 수행"""
        y = x.right if x else None
        T2 = y.left if y else None
        if y:
            y.left = x
        x.right = T2
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        if y:
            y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y

    def insert(self, node, key, size):
        """새 노드를 AVL 트리에 삽입"""
        if not node:
            return AVLTreeNode(key, size)
        if key < node.key:
            node.left = self.insert(node.left, key, size)
        else:
            node.right = self.insert(node.right, key, size)
        
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        balance = self.get_balance(node)
        
        # 왼쪽-왼쪽 케이스
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)
        # 오른쪽-오른쪽 케이스
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)
        # 왼쪽-오른쪽 케이스
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        # 오른쪽-왼쪽 케이스
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node

    def delete(self, root, key):
        """노드를 AVL 트리에서 삭제"""
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.size = temp.size
            root.right = self.delete(root.right, temp.key)
        
        if not root:
            return root
        
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        balance = self.get_balance(root)
        
        # 왼쪽-왼쪽 케이스
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        # 왼쪽-오른쪽 케이스
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # 오른쪽-오른쪽 케이스
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        # 오른쪽-왼쪽 케이스
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root

    def get_min_value_node(self, node):
        """트리에서 최소 값 노드를 찾음"""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_best_fit(self, node, size):
        """주어진 크기에 가장 적합한 노드를 찾음"""
        if not node:
            return None, None
        if node.size >= size:
            best_fit_left, best_fit_left_node = self.find_best_fit(node.left, size)
            if best_fit_left is None or (node.size < best_fit_left_node.size):
                return node.key, node
            return best_fit_left, best_fit_left_node
        return self.find_best_fit(node.right, size)

    def insert_node(self, key, size):
        """주어진 키와 크기의 노드를 삽입"""
        self.root = self.insert(self.root, key, size)

    def delete_node(self, key):
        """주어진 키의 노드를 삭제"""
        self.root = self.delete(self.root, key)

    def find_best_fit_node(self, size):
        """주어진 크기에 가장 적합한 노드를 반환"""
        return self.find_best_fit(self.root, size)
    
#=========================================================================================

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

    def insert_interval(self, low, high):
        """새 구간을 간격 트리에 삽입"""
        self.root = self.insert(self.root, low, high)

    def delete_interval(self, low, high):
        """구간을 간격 트리에서 삭제"""
        self.root = self.delete(self.root, low, high)

    def find_overlap(self, low, high):
        """주어진 구간과 겹치는 구간을 찾음"""
        return self.overlap_search(self.root, low, high)
    
    #========================================================================

class Allocator:
    def __init__(self):
        self.chunk_size = 4096  # 기본 청크 크기
        self.arena = []  # 할당된 청크를 저장할 리스트
        self.free_list = {  # 크기별로 분리된 free list
            (0, 128): AVLTree(),
            (128, 512): AVLTree(),
            (512, 1024): AVLTree(),
            (1024, 2048): AVLTree(),
            (2048, 4096): AVLTree(),
            (4096, float('inf')): AVLTree()
        }
        self.allocations = {}  # 할당된 메모리를 저장할 딕셔너리
        self.interval_tree = IntervalTree()  # 간격 트리
        self.start_time = time.time()  # 성능 측정을 위한 시작 시간 기록

    def get_free_list_range(self, size):
        """주어진 크기가 들어갈 범위를 반환"""
        for key in self.free_list:
            if key[0] < size <= key[1]:
                return key
        return None

    def malloc(self, id, size):
        """주어진 크기의 메모리를 할당하고 id와 연관"""
        #1.주어진 크기에 적합한 범위를 찾음
        range_key = self.get_free_list_range(size)
        if not range_key:
            return None
        #2. 적합한 범위에서 free tree를 가져옴 
        free_tree = self.free_list[range_key]
        #3. free tree에서 주어진 크기에 가장 적합한 노드 찾기
        best_fit_key, best_fit_node = free_tree.find_best_fit_node(size)
        if best_fit_node:
            #4.가장 적합한 노드찾은경우 free_tree에서 해당 노드 삭제 하고 메모리할당
            free_tree.delete_node(best_fit_key)
            #할당된 메모리 블록의 시작 주소와 크기를 allocations 딕셔너리에 저장
            self.allocations[id] = (best_fit_key, size)
            #5. 할당하고 남은 잔여공간 적절한 범위의 free tree 찾아 삽입
            if best_fit_node.size > size:
                remaining_size = best_fit_node.size - size
                remaining_key = best_fit_key + size
                remaining_range = self.get_free_list_range(remaining_size)
                if remaining_range:
                    self.free_list[remaining_range].insert_node(remaining_key, remaining_size)

        #적합한 노드 찾지 못한 경우, 새로운 청크할당
        ##여기서 살짝수정이 필요해서  test 4로 넘어가겠음 .
        else:
            new_chunk_key = len(self.arena) * self.chunk_size
            self.arena.append(bytearray(self.chunk_size))
            remaining_size = self.chunk_size - size
            self.allocations[id] = (new_chunk_key, size)
            if remaining_size > 0:
                remaining_key = new_chunk_key + size
                remaining_range = self.get_free_list_range(remaining_size)
                if remaining_range:
                    self.free_list[remaining_range].insert_node(remaining_key, remaining_size)

    def free(self, id):
        """주어진 id와 연관된 메모리를 해제"""
        if id in self.allocations:
            start, size = self.allocations.pop(id)
            end = start + size
            self.interval_tree.insert_interval(start, end)
            range_key = self.get_free_list_range(size)
            self.free_list[range_key].insert_node(start, size)
            overlap_node = self.interval_tree.find_overlap(start, end)
            if overlap_node:
                self.interval_tree.delete_interval(overlap_node.low, overlap_node.high)
                merged_start = min(start, overlap_node.low)
                merged_end = max(end, overlap_node.high)
                merged_size = merged_end - merged_start
                merged_range = self.get_free_list_range(merged_size)
                if merged_range:
                    self.free_list[merged_range].insert_node(merged_start, merged_size)

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
    
    with open("allocator\inputdata.txt", "r") as file:
        n = 0
        for line in file:
            req = line.split()
            if req[0] == 'a':
                allocator.malloc(int(req[1]), int(req[2]))  # 메모리 할당 요청 처리
            elif req[0] == 'f':
                allocator.free(int(req[1]))  # 메모리 해제 요청 처리

            # if n%100 == 0:
            #     print(n, "...")
            
            n += 1
    
    allocator.print_stats()  # 메모리 사용 통계 출력
